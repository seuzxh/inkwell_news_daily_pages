#!/usr/bin/env python3
"""获取 InkWell 0618 文章详情"""
import json
import re
from pathlib import Path

# 所有文章 ID
ARTICLE_IDS = [
    "art_ntuxpq", "art_5sehi7", "art_li0w5o", "art_bfzoxu", "art_f8ivt0",
    "art_w1mhhi", "art_x5d124", "art_x2qv2k", "art_7atrmg", "art_qgwekj",
    "art_1wizgx", "art_18ixrz", "art_3j9zw2", "art_c3m1lk", "art_hjnqfi",
    "art_ywnbv8", "art_k377s3", "art_955kc4", "art_ijmbo9", "art_31vduh",
    "art_7uaswf", "art_q1lqh6", "art_w6gzhi", "art_kx9yqk"
]

# 从浏览器获取的基本信息（分类/标题/摘要）
BASIC_INFO = {
    "art_ntuxpq": {"category": "Tech Culture", "title": "Pluralistic: The (real) dead economy theory (17 Jun 2026)", "source": "pluralistic.net"},
    "art_5sehi7": {"category": "AI & ML", "title": "🔬 The Self-Driving Lab — Joseph Krause, Radical AI", "source": "Latent Space"},
    "art_li0w5o": {"category": "Tech Culture", "title": "You Got Faster. Your Company Didn't.", "source": "terriblesoftware.org"},
    "art_bfzoxu": {"category": "AI & ML", "title": "Quoting Charity Majors", "source": "simonwillison.net"},
    "art_f8ivt0": {"category": "Programming", "title": "Logic for Programmers v0.15, Livecoding", "source": "buttondown.com/hillelwayne"},
    "art_w1mhhi": {"category": "Essays", "title": "Formalizing a ring theorem with Lean 4 and Claude", "source": "johndcook.com"},
    "art_x5d124": {"category": "Indie", "title": "Summoning the Demon", "source": "geohot.github.io"},
    "art_x2qv2k": {"category": "AI & ML", "title": "[AINews] GLM-5.2: the top Frontend Coding model in the world", "source": "Latent Space"},
    "art_7atrmg": {"category": "AI & ML", "title": "<click-to-play> — a still that plays", "source": "simonwillison.net"},
    "art_qgwekj": {"category": "AI & ML", "title": "NetNewsWire Status", "source": "simonwillison.net"},
    "art_1wizgx": {"category": "Indie", "title": "Flax debugging: making a hash of things", "source": "gilesthomas.com"},
    "art_18ixrz": {"category": "AI & ML", "title": "datasette 1.0a34", "source": "simonwillison.net"},
    "art_3j9zw2": {"category": "AI & ML", "title": "Unlocking UK house-building with AI-accelerated planning", "source": "Google DeepMind"},
    "art_c3m1lk": {"category": "Indie", "title": "Debugging on Prod", "source": "idiallo.com"},
    "art_hjnqfi": {"category": "Web & Design", "title": "Key, in sight", "source": "aresluna.org"},
    "art_ywnbv8": {"category": "Indie", "title": "10Gb/s Ethernet: switching to a Broadcom SFP+ module", "source": "gilesthomas.com"},
    "art_k377s3": {"category": "Essays", "title": "Partial fraction decomposition", "source": "johndcook.com"},
    "art_955kc4": {"category": "AI & ML", "title": "datasette-tailscale 0.1a0", "source": "simonwillison.net"},
    "art_ijmbo9": {"category": "AI & ML", "title": "Quoting Georgi Gerganov", "source": "simonwillison.net"},
    "art_31vduh": {"category": "Systems", "title": "Do not invite big-tech to join your digital autonomy discussion", "source": "berthub.eu"},
    "art_7uaswf": {"category": "Systems", "title": "Retrofitting the WM_COPY­DATA message onto Windows 3.1", "source": "devblogs.microsoft.com/oldnewthing"},
    "art_q1lqh6": {"category": "AI & ML", "title": "Would you like a drainer served at the very top of DuckDuckGo?", "source": "timsh.org"},
    "art_w6gzhi": {"category": "Essays", "title": "Lean Launch Pad 2026 @ Stanford – Lessons Learned Presentations", "source": "steveblank.com"},
    "art_kx9yqk": {"category": "Tech Culture", "title": "Two Way TV - product photos of 1997's hottest gadget", "source": "shkspr.mobi"}
}

# Inkwell 文章页URL格式
BASE_URL = "https://inkwell.coze.com/article/"

# 生成完整数据
articles = []
for aid in ARTICLE_IDS:
    info = BASIC_INFO.get(aid, {})
    articles.append({
        "id": aid,
        "url": BASE_URL + aid,
        "title": info.get("title", ""),
        "category": info.get("category", ""),
        "source": info.get("source", "")
    })

# 保存
output = Path("./data/2026/06/18_articles.json")
output.parent.mkdir(parents=True, exist_ok=True)
with open(output, 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"保存了 {len(articles)} 篇文章到 {output}")
