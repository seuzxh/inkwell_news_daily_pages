# Inkwell 资讯归档系统

极简的每日资讯归档系统，支持 GitHub Pages 静态托管。

## 文件结构

```
inkwell-archive/
├── index.html      # 首页，展示最新一天资讯
├── archive.html    # 归档页，按日期倒序列出所有资讯
├── date.html       # 日期详情页
├── style.css       # 极简样式
├── add_news.py     # 资讯添加脚本
└── data/           # Markdown 数据存储
    └── 2026/
        └── 05/
            └── 05.md
```

## 快速开始

### 1. 本地预览

直接用浏览器打开 `index.html` 即可查看。

### 2. 添加新资讯

#### 方式一：使用脚本（推荐）

```bash
# 添加单条资讯
python add_news.py --date 2026-05-06 --ai-tech "标题|摘要"

# 添加多条资讯（不同分类）
python add_news.py --date 2026-05-06 \
    --ai-tech "标题1|摘要1" \
    --ai-tech "标题2|摘要2" \
    --research "研究标题|摘要" \
    --market "市场动态|摘要"

# 同步所有 Markdown 到 HTML
python add_news.py --sync
```

#### 方式二：手动编辑

1. 创建 Markdown 文件：`data/2026/05/06.md`
2. 按以下格式编写：

```markdown
# Inkwell 资讯 - 2026年5月6日

## AI 科技

- **新闻标题**
  一句话摘要内容。

## 投研

- **研究报告标题**
  摘要内容。

## 市场动态

- **市场动态标题**
  摘要内容。
```

3. 运行 `python add_news.py --sync` 同步到 HTML

### 3. 部署到 GitHub Pages

1. **创建 GitHub 仓库**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **推送到 GitHub**
   ```bash
   git remote add origin https://github.com/用户名/仓库名.git
   git push -u origin main
   ```

3. **启用 GitHub Pages**
   - 进入仓库 Settings → Pages
   - Source 选择 `main` branch
   - 等待部署完成

4. **访问你的站点**
   - 地址：`https://用户名.github.io/仓库名/`

## 分类说明

- **AI 科技**：AI 产品、技术进展发布
- **投研**：研究报告、学术论文、行业分析
- **市场动态**：资本市场、公司财报、投资融资

## 自定义

### 修改网站标题

编辑 `index.html` 和 `archive.html`，修改：
```html
<h1 class="site-title"><a href="index.html">你的网站名</a></h1>
```

### 修改网站描述

编辑 HTML 文件中的副标题：
```html
<p class="site-subtitle">你的描述</p>
```

### 修改颜色主题

编辑 `style.css`，修改 `.category-title` 相关颜色：
```css
.category-title.ai-tech { color: #0066cc; border-color: #0066cc; }
.category-title.research { color: #7c3aed; border-color: #7c3aed; }
.category-title.market { color: #059669; border-color: #059669; }
```

## 注意事项

- 所有日期使用 `YYYY-MM-DD` 格式
- 资讯数据存储在 `data/` 目录的 Markdown 文件中
- 修改 Markdown 文件后需运行 `python add_news.py --sync` 同步
- HTML 文件包含内嵌的 JavaScript 数据，更新后可直接部署

## License

MIT
