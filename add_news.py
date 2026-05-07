#!/usr/bin/env python3
"""
Inkwell 资讯添加脚本

用于自动生成每日资讯的 Markdown 文件和更新 HTML 页面数据。

使用方法:
    # 添加单条资讯
    python add_news.py --date 2026-05-06 --category ai_tech \
        --title "新闻标题" --summary "一句话摘要"

    # 添加多条资讯
    python add_news.py --date 2026-05-06 \
        --ai-tech "标题1|摘要1" \
        --ai-tech "标题2|摘要2" \
        --research "标题|摘要" \
        --market "标题|摘要"

    # 更新所有 HTML 页面的数据
    python add_news.py --sync

    # 生成完整列表 HTML
    python add_news.py --complete 2026-05-06

    # 查看帮助
    python add_news.py --help
"""

import argparse
import os
import re
import json
from datetime import datetime
from pathlib import Path

# 脚本所在目录
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR / "data"
HTML_FILES = [
    SCRIPT_DIR / "index.html",
    SCRIPT_DIR / "archive.html",
    SCRIPT_DIR / "date.html"
]
COMPLETE_HTML = SCRIPT_DIR / "complete.html"

# 分类映射（精选页）
CATEGORIES = {
    "ai_tech": ("AI 科技", "ai-tech"),
    "research": ("投研", "research"),
    "market": ("市场动态", "market"),
}

# 完整列表分类映射
COMPLETE_CATEGORIES = {
    "tech": ("科技", "tech"),
    "product": ("产品", "product"),
    "finance": ("金融", "finance"),
    "other": ("其他", "other"),
}

# 星期映射
WEEKDAYS = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]


def parse_date(date_str):
    """解析日期字符串，返回年、月、日"""
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.year, dt.month, dt.day, dt.weekday()
    except ValueError:
        raise ValueError(f"日期格式错误，请使用 YYYY-MM-DD 格式: {date_str}")


def ensure_data_dir(year, month):
    """确保数据目录存在"""
    data_path = DATA_DIR / str(year) / f"{month:02d}"
    data_path.mkdir(parents=True, exist_ok=True)
    return data_path


def generate_markdown(date_str, news_items):
    """生成 Markdown 文件内容"""
    year, month, day, weekday = parse_date(date_str)
    date_display = f"{year}年{month}月{day}日"
    
    lines = [
        f"# Inkwell 资讯 - {date_display}",
        "",
    ]
    
    for cat_key, (cat_name, _) in CATEGORIES.items():
        if cat_key in news_items and news_items[cat_key]:
            lines.append(f"## {cat_name}")
            lines.append("")
            for item in news_items[cat_key]:
                lines.append(f"- **{item['title']}**")
                lines.append(f"  {item['summary']}")
                lines.append("")
    
    return "\n".join(lines)


def save_markdown(date_str, content):
    """保存 Markdown 文件"""
    year, month, day, weekday = parse_date(date_str)
    data_path = ensure_data_dir(year, month)
    md_file = data_path / f"{day:02d}.md"
    md_file.write_text(content, encoding="utf-8")
    return md_file


def parse_news_item(item_str):
    """解析资讯字符串 '标题|摘要'"""
    parts = item_str.split("|")
    if len(parts) < 2:
        raise ValueError(f"资讯格式错误，应为 '标题|摘要': {item_str}")
    return {"title": parts[0].strip(), "summary": parts[1].strip()}


def collect_all_news():
    """收集所有 Markdown 文件中的资讯"""
    news_data = {}
    
    if not DATA_DIR.exists():
        return news_data
    
    # 遍历所有日期目录
    for year_dir in sorted(DATA_DIR.iterdir(), reverse=True):
        if not year_dir.is_dir():
            continue
        for month_dir in sorted(year_dir.iterdir(), reverse=True):
            if not month_dir.is_dir():
                continue
            for md_file in sorted(month_dir.glob("*.md"), reverse=True):
                date_str = f"{year_dir.name}-{month_dir.name}-{md_file.stem}"
                news_data[date_str] = parse_markdown_file(md_file)
    
    return news_data


def parse_markdown_file(md_file):
    """解析 Markdown 文件"""
    content = md_file.read_text(encoding="utf-8")
    
    # 从文件名提取日期
    date_match = re.search(r"(\d{4})-(\d{2})-(\d{2})", str(md_file))
    if not date_match:
        return None
    
    year, month, day = date_match.groups()
    date_str = f"{year}-{month}-{day}"
    dt = datetime(int(year), int(month), int(day))
    
    news = {
        "date": f"{year}年{int(month)}月{int(day)}日",
        "weekday": WEEKDAYS[dt.weekday()],
        "ai_tech": [],
        "research": [],
        "market": []
    }
    
    current_category = None
    lines = content.split("\n")
    
    for line in lines:
        # 检测分类
        if line.startswith("## "):
            cat_name = line[3:].strip()
            if cat_name == "AI 科技":
                current_category = "ai_tech"
            elif cat_name == "投研":
                current_category = "research"
            elif cat_name == "市场动态":
                current_category = "market"
            else:
                current_category = None
        # 解析资讯
        elif line.startswith("- **") and current_category:
            title_match = re.search(r"- \*\*(.+?)\*\*", line)
            if title_match:
                news[current_category].append({
                    "title": title_match.group(1),
                    "summary": ""
                })
        elif news[current_category] and len(news[current_category][-1]["summary"]) == 0:
            # 摘要行（缩进的普通文本）
            if line.strip().startswith("- "):
                summary = line.strip()[2:].strip()
                if summary:
                    news[current_category][-1]["summary"] = summary
            elif line.strip() and not line.startswith("#"):
                news[current_category][-1]["summary"] = line.strip()
    
    return news


def generate_js_data(news_data):
    """生成 JavaScript 数据"""
    return json.dumps(news_data, ensure_ascii=False, indent=2)


def update_html_files(news_data):
    """更新所有 HTML 文件中的数据"""
    js_data = generate_js_data(news_data)
    
    for html_file in HTML_FILES:
        if not html_file.exists():
            print(f"警告: 文件不存在 {html_file}")
            continue
        
        content = html_file.read_text(encoding="utf-8")
        
        # 替换 newsData 变量
        pattern = r"// 资讯数据\s*const newsData = \{[\s\S]*?\};"
        replacement = f"// 资讯数据\n    const newsData = {js_data};"
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content == content:
            # 可能没有现有数据，尝试在其他位置插入
            if "// 资讯数据" in content:
                new_content = content.replace(
                    "// 资讯数据",
                    f"// 资讯数据\n    const newsData = {js_data};"
                ).split(";// 资讯数据")[0] + ";"
        
        html_file.write_text(new_content, encoding="utf-8")
        print(f"已更新: {html_file.name}")


def generate_complete_html(date_str, news_data):
    """生成完整列表页面的 HTML 内容"""
    date_key = date_str
    data = news_data.get(date_key)
    
    if not data:
        return None
    
    # 将精选数据映射到完整列表分类
    complete_data = {
        "date": data["date"],
        "weekday": data["weekday"],
        "tech": list(data.get("ai_tech", [])),  # AI 科技 -> 科技
        "product": [],  # 产品分类需要单独添加
        "finance": list(data.get("market", [])),  # 市场动态 -> 金融
        "other": list(data.get("research", []))  # 投研 -> 其他
    }
    
    js_data = json.dumps({date_key: complete_data}, ensure_ascii=False, indent=2)
    
    # 读取现有 complete.html
    if not COMPLETE_HTML.exists():
        print(f"警告: complete.html 不存在，跳过更新")
        return
    
    content = COMPLETE_HTML.read_text(encoding="utf-8")
    
    # 替换 completeNewsData 变量
    pattern = r"// 完整资讯数据.*const completeNewsData = \{[\s\S]*?\};"
    replacement = f"// 完整资讯数据（从 Markdown 解析的完整数据）\n    const completeNewsData = {js_data};"
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content == content:
        print(f"警告: 无法更新 completeNewsData，请检查文件格式")
        return
    
    COMPLETE_HTML.write_text(new_content, encoding="utf-8")
    print(f"已更新: complete.html ({date_str} 完整列表)")


def main():
    parser = argparse.ArgumentParser(
        description="Inkwell 资讯添加脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 添加资讯
  python add_news.py --date 2026-05-06 --ai-tech "OpenAI发布新模型|性能大幅提升"
  python add_news.py --date 2026-05-06 --research "新研究发布|突破性进展" --market "市场动态|值得关注"

  # 同步所有 Markdown 到 HTML
  python add_news.py --sync

  # 生成指定日期的完整列表 HTML
  python add_news.py --complete 2026-05-06

  # 列出所有资讯
  python add_news.py --list
        """
    )
    
    parser.add_argument("--date", help="日期 (YYYY-MM-DD)")
    parser.add_argument("--ai-tech", action="append", help="AI科技资讯 (标题|摘要)")
    parser.add_argument("--research", action="append", help="投研资讯 (标题|摘要)")
    parser.add_argument("--market", action="append", help="市场动态资讯 (标题|摘要)")
    parser.add_argument("--sync", action="store_true", help="同步所有 Markdown 数据到 HTML")
    parser.add_argument("--complete", metavar="DATE", help="生成指定日期的完整列表 HTML (YYYY-MM-DD)")
    parser.add_argument("--list", action="store_true", help="列出所有资讯")
    
    args = parser.parse_args()
    
    # 列出所有资讯
    if args.list:
        news_data = collect_all_news()
        if not news_data:
            print("暂无资讯")
            return
        
        for date_key in sorted(news_data.keys(), reverse=True):
            news = news_data[date_key]
            if news:
                total = len(news.get("ai_tech", [])) + len(news.get("research", [])) + len(news.get("market", []))
                print(f"\n{news['date']} ({news['weekday']}) - {total} 条资讯")
        return
    
    # 生成完整列表 HTML
    if args.complete:
        print(f"正在生成完整列表 HTML: {args.complete}")
        news_data = collect_all_news()
        generate_complete_html(args.complete, news_data)
        return
    
    # 同步数据
    if args.sync:
        print("正在同步所有资讯数据...")
        news_data = collect_all_news()
        update_html_files(news_data)
        print(f"\n已同步 {len(news_data)} 天的资讯数据")
        return
    
    # 添加新资讯
    if not args.date:
        parser.error("--date 参数必填")
    
    news_items = {}
    
    for cat_key, (cat_name, _) in CATEGORIES.items():
        items = getattr(args, cat_key, None)
        if items:
            news_items[cat_key] = [parse_news_item(item) for item in items]
    
    if not news_items:
        parser.error("请至少添加一条资讯 (--ai-tech, --research 或 --market)")
    
    # 生成 Markdown
    year, month, day, weekday = parse_date(args.date)
    date_display = f"{year}年{month}月{day}日"
    
    md_content = generate_markdown(args.date, news_items)
    md_file = save_markdown(args.date, md_content)
    
    print(f"✓ 已生成 Markdown 文件: {md_file}")
    print(f"\n日期: {date_display} {WEEKDAYS[weekday]}")
    for cat_key, (cat_name, _) in CATEGORIES.items():
        if cat_key in news_items:
            print(f"  {cat_name}: {len(news_items[cat_key])} 条")
    
    # 询问是否同步到 HTML
    sync = input("\n是否同步到 HTML 页面? (y/N): ").strip().lower()
    if sync == "y":
        news_data = collect_all_news()
        update_html_files(news_data)
        print(f"\n已同步 {len(news_data)} 天的资讯数据")


if __name__ == "__main__":
    main()
