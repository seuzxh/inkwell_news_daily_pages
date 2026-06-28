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
                # 去掉 _complete 后缀，确保日期格式正确
                date_str = date_str.replace('_complete', '')
                news_data[date_str] = parse_markdown_file(md_file)
    
    return news_data


def parse_markdown_file(md_file):
    """解析 Markdown 文件，支持新旧两种格式"""
    content = md_file.read_text(encoding="utf-8")
    
    # 获取 md_file 的绝对路径用于计算索引
    abs_md_file = md_file.resolve() if not md_file.is_absolute() else md_file
    
    # md_file 的路径相对于 DATA_DIR
    try:
        # 获取 md_file 相对于 DATA_DIR 的路径部分
        rel_parts = abs_md_file.relative_to(DATA_DIR).parts
        if len(rel_parts) >= 3:
            year = rel_parts[0]
            month = rel_parts[1]
            day = rel_parts[2].replace('.md', '').replace('_complete', '')
        else:
            return None
    except ValueError:
        # 如果 relative_to 失败，使用绝对路径
        data_dir_parts = len(DATA_DIR.parts)
        year = abs_md_file.parts[data_dir_parts]
        month = abs_md_file.parts[data_dir_parts + 1]
        day = abs_md_file.parts[data_dir_parts + 2].replace('.md', '').replace('_complete', '')
    
    # 验证年份格式
    if not year.isdigit() or len(year) != 4:
        return None
    
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)
    dt = datetime(year_int, month_int, day_int)
    
    # 处理 _complete 后缀的文件名
    is_complete = "_complete" in md_file.stem
    
    # 检查是否是完整列表（通过文件名中的 _complete 标记或分类判断）
    # 新格式分类：## AI & ML（7篇）或 ## AI & ML
    new_format_categories = ["AI & ML", "Programming", "Systems", "Essays", "Tech Culture", "Indie", "Product", "Data"]
    has_new_format = any(cat in content for cat in new_format_categories)
    
    if is_complete or has_new_format:
        # 新格式（完整列表或精选）：## AI & ML（7篇）或 ## AI & ML
        return parse_new_format(content, year, month, day, dt)
    else:
        # 旧格式：## AI 科技
        return parse_old_format(content, year, month, day, dt)


def parse_old_format(content, year, month, day, dt):
    """解析旧格式 Markdown 文件（## AI 科技, - **标题**）"""
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
                    "summary": "",
                    "link": "",
                    "category": current_category
                })
        elif news.get(current_category) and len(news[current_category]) > 0 and len(news[current_category][-1]["summary"]) == 0:
            # 摘要行（缩进的普通文本）
            if line.strip().startswith("- "):
                summary = line.strip()[2:].strip()
                if summary:
                    news[current_category][-1]["summary"] = summary
            elif line.strip() and not line.startswith("#"):
                news[current_category][-1]["summary"] = line.strip()
    
    return news


def parse_new_format(content, year, month, day, dt):
    """解析新格式 Markdown 文件（## AI & ML, **标题**, ▸ 描述, 🔗 链接）"""
    
    # 分类映射（新格式英文/中文 -> 旧格式中文）
    category_mapping = {
        # 英文分类
        "ai & ml": "ai_tech",
        "programming": "research",
        "systems": "market",
        "essays": "ai_tech",
        "tech culture": "research",
        "indie": "market",
        "product": "ai_tech",
        "finance": "market",
        "data": "research",
        # 中文分类（Inkwell实际输出格式）
        "ai 科技": "ai_tech",
        "ai科技": "ai_tech",
        "投研": "research",
        "市场动态": "market",
        "科技": "ai_tech",
        "产品": "ai_tech",
        "金融": "market",
        "其他": "research",
    }
    
    news = {
        "date": f"{year}年{int(month)}月{int(day)}日",
        "weekday": WEEKDAYS[dt.weekday()],
        "ai_tech": [],
        "research": [],
        "market": []
    }
    
    current_category = None
    lines = content.split("\n")
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # 检测分类（## AI & ML 或 ## AI & ML（7篇））
        if line.startswith("## "):
            cat_match = re.search(r"##\s+([\w\s&]+?)(?:（|\(|$)", line)
            if cat_match:
                cat_name = cat_match.group(1).strip().lower()
                current_category = category_mapping.get(cat_name)
            else:
                current_category = None
            i += 1
            continue
        
        # 解析标题（支持三种格式）
        # 格式0: 编号列表 "1. **标题**" 或 "1. **标题**（注释）"（0625起新格式）
        m_num = re.match(r"^\d+\.\s*\*\*(.+?)\*\*", line)
        if m_num and current_category:
            title = m_num.group(1).strip()
            # 去掉标题末尾的 emoji 和 （xxx推荐）等装饰
            title = re.sub(r"\s*（[^）]*）\s*$", "", title)
            summary = ""
            link = ""

            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if re.match(r"^\d+\.\s*\*\*", next_line) or next_line.startswith("## ") or next_line.startswith("---"):
                    break
                # 0625+ 格式：- 摘要：xxx / - 原文：xxx / - 描述：xxx
                if next_line.startswith("- 摘要：") or next_line.startswith("- 摘要:") or next_line.startswith("摘要：") or next_line.startswith("摘要:"):
                    summary = re.sub(r"^[-\s]*摘要[:：]\s*", "", next_line)
                elif next_line.startswith("- 描述：") or next_line.startswith("- 描述:"):
                    summary = re.sub(r"^[-\s]*描述[:：]\s*", "", next_line)
                elif next_line.startswith("- 原文：") or next_line.startswith("- 原文:") or next_line.startswith("原文：") or next_line.startswith("原文:"):
                    lm = re.search(r"(https?://\S+)", next_line)
                    if lm and not link:
                        link = lm.group(1)
                # 兼容老 ▸ / 🔗 标记
                elif next_line.startswith("▸"):
                    if not summary:
                        summary = next_line[1:].strip()
                elif next_line.startswith("🔗"):
                    lm = re.search(r"(https?://\S+)", next_line)
                    if lm and not link:
                        link = lm.group(1)
                i += 1

            if title:
                news[current_category].append({
                    "title": title, "summary": summary, "link": link, "category": current_category
                })
            continue

        # 格式1: **标题**（兼容新旧两种子格式）
        if line.startswith("**") and line.endswith("**") and current_category:
            title = line[2:-2].strip()
            summary = ""
            link = ""
            
            # 继续读取描述和链接
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                
                # 遇到下一个标题或分类，停止
                if next_line.startswith("**") or next_line.startswith("## ") or next_line.startswith("---") or re.match(r"^\d+\.\s*\*\*", next_line):
                    break
                
                # 解析描述 ▸ 描述
                if next_line.startswith("▸"):
                    summary = next_line[1:].strip()
                # 0623 格式：- 摘要: xxx
                elif next_line.startswith("- 摘要:") or next_line.startswith("- 摘要：") or next_line.startswith("摘要：") or next_line.startswith("摘要:"):
                    if not summary:
                        summary = re.sub(r"^[-\s]*摘要[:：]\s*", "", next_line)
                # 0623 格式：- 原文: https://...
                elif next_line.startswith("- 原文:") or next_line.startswith("- 原文：") or next_line.startswith("原文：") or next_line.startswith("原文:"):
                    lm = re.search(r"(https?://\S+)", next_line)
                    if lm and not link:
                        link = lm.group(1)
                # 解析链接 🔗 链接
                elif next_line.startswith("🔗"):
                    link_match = re.search(r"🔗\s*(https?://\S+)", next_line)
                    if link_match:
                        link = link_match.group(1)
                    # 也检查纯 URL
                    elif next_line.startswith("http"):
                        link = next_line
                elif next_line.startswith("来源：") or next_line.startswith("发布时间：") or next_line.startswith("- 来源:") or next_line.startswith("- Inkwell:"):
                    # 忽略元信息
                    pass
                
                i += 1
            
            # 添加资讯
            if title:
                news[current_category].append({
                    "title": title,
                    "summary": summary,
                    "link": link,
                    "category": current_category
                })
            continue
        
        # 格式2: 【标题】  (完整列表格式)
        if line.startswith("【") and "】" in line and current_category:
            # 提取标题（去除【】和emoji）
            title = re.sub(r"^【|】$", "", line).strip()
            # 清理标题中的 emoji
            title = re.sub(r"[\U0001F300-\U0001F9FF]", "", title).strip()
            
            summary = ""
            link = ""
            
            # 继续读取描述和链接
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                
                # 遇到下一个标题或分类，停止
                if next_line.startswith("【") or next_line.startswith("## ") or next_line.startswith("---"):
                    break
                
                # 解析链接 原文链接：https://...
                if "原文链接：" in next_line:
                    link_match = re.search(r"原文链接：\s*(https?://\S+)", next_line)
                    if link_match:
                        link = link_match.group(1)
                elif next_line.startswith("http"):
                    link = next_line
                
                i += 1
            
            # 添加资讯
            if title:
                news[current_category].append({
                    "title": title,
                    "summary": summary,
                    "link": link,
                    "category": current_category
                })
            continue
        
        i += 1
    
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
        
        # 找到第一个正确的 newsData 声明（前面有 // 资讯数据）
        correct_pattern = r"// 资讯数据\s*\n\s*const newsData = \{[\s\S]*?\};"
        correct_match = re.search(correct_pattern, content)
        
        if correct_match:
            # 保留正确块之前的内容
            before = content[:correct_match.start()]
            correct_end = correct_match.end()
            after = content[correct_end:]
            
            # 删除正确块之后的所有旧 newsData 声明
            after_clean = re.sub(r"\s*// 资讯数据\s*\n\s*const newsData = \{[\s\S]*?\};", "", after)
            after_clean = re.sub(r"\s*const newsData = \{[\s\S]*?\};", "", after_clean)
            
            # 替换为新的数据
            new_data_block = f"// 资讯数据\n    const newsData = {js_data};"
            content = before + new_data_block + after_clean
        else:
            # 如果没有正确的声明，清理所有旧声明并添加新的
            content = re.sub(r"// 资讯数据\s*\n?\s*const newsData = \{[\s\S]*?\};", "", content)
            content = re.sub(r"const newsData = \{[\s\S]*?\};", "", content)
            
            if "// 资讯数据" in content:
                new_data_block = f"// 资讯数据\n    const newsData = {js_data};"
                content = content.replace("// 资讯数据", new_data_block)
            else:
                content = content.replace("<script>", f"<script>\n    // 资讯数据\n    const newsData = {js_data};")
        
        html_file.write_text(content, encoding="utf-8")
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
    pattern = r'// 完整资讯数据[^\n]*\n\s*const completeNewsData = \{[\s\S]*?\};'
    replacement = f'// 完整资讯数据（从 Markdown 解析的完整数据）\n    const completeNewsData = {js_data};'
    
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
        # 一次性把所有日期写入 complete.html（修复多天覆盖 bug）
        all_complete = {}
        for date_key, data in news_data.items():
            all_complete[date_key] = {
                "date": data["date"],
                "weekday": data["weekday"],
                "tech": list(data.get("ai_tech", [])),
                "product": [],
                "finance": list(data.get("market", [])),
                "other": list(data.get("research", [])),
            }
        if COMPLETE_HTML.exists() and all_complete:
            content = COMPLETE_HTML.read_text(encoding="utf-8")
            js_data = json.dumps(all_complete, ensure_ascii=False, indent=2)
            pattern = r'// 完整资讯数据[^\n]*\n\s*const completeNewsData = \{[\s\S]*?\};'
            replacement = f'// 完整资讯数据（从 Markdown 解析的完整数据）\n    const completeNewsData = {js_data};'
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                COMPLETE_HTML.write_text(new_content, encoding="utf-8")
                print(f"已更新: complete.html ({len(all_complete)} 天完整列表)")
            else:
                print("警告: complete.html 模式匹配失败，未更新")
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
