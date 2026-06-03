#!/usr/bin/env python3
"""批量获取 InkWell 文章详情"""

import json
import subprocess
import re

# 24篇文章数据
ARTICLES_DATA = [
    {"url": "https://inkwell.coze.com/article/art_p28uzh", "title": "Is datacentre sovereignty really that important?", "meta": "Indie · / · martinalderson.com · · · martin@martinalderson.com (Martin Alderson)"},
    {"url": "https://inkwell.coze.com/article/art_pvdd2g", "title": "Now that your newsletter is AI-generated, I've Unsubscribed", "meta": "Indie · / · idiallo.com · · · rss@idiallo.com"},
    {"url": "https://inkwell.coze.com/article/art_strk50", "title": "🔬Scaling Past Informal AI - Carina Hong, Axiom Math", "meta": "AI & ML · / · Latent Space · · · RJ Honicky"},
    {"url": "https://inkwell.coze.com/article/art_dj3gbf", "title": "⚡️Satya Nadella: No Priors x Latent Space Crossover Special at Microsoft Build", "meta": "AI & ML · / · Latent Space"},
    {"url": "https://inkwell.coze.com/article/art_vrdx5c", "title": "Naively summing an alternating series", "meta": "Essays · / · johndcook.com · · · John"},
    {"url": "https://inkwell.coze.com/article/art_rjaiwy", "title": "Skills Registry Threat Models", "meta": "Indie · / · nesbitt.io · · · Andrew Nesbitt"},
    {"url": "https://inkwell.coze.com/article/art_l7qxm2", "title": "Uber Caps Usage of AI Tools Like Claude Code to Manage Costs", "meta": "AI & ML · / · simonwillison.net"},
    {"url": "https://inkwell.coze.com/article/art_p3lwi4", "title": "London Data Store Relaunch", "meta": "Tech Culture · / · shkspr.mobi · · · @edent"},
    {"url": "https://inkwell.coze.com/article/art_qs26xv", "title": "Quoting Natalie Lung", "meta": "AI & ML · / · simonwillison.net"},
    {"url": "https://inkwell.coze.com/article/art_h9prfw", "title": "[AINews] Microsoft Build: MAI-Thinking-1 and MAI Family models", "meta": "AI & ML · / · Latent Space"},
    {"url": "https://inkwell.coze.com/article/art_jfdhoz", "title": "Welcoming the Philippine Government to Have I Been Pwned", "meta": "Security · / · troyhunt.com · · · Troy Hunt"},
    {"url": "https://inkwell.coze.com/article/art_y3zgdt", "title": "A survey of inlining heuristics", "meta": "Programming · / · bernsteinbear.com"},
    {"url": "https://inkwell.coze.com/article/art_bpaodo", "title": "Microsoft's new MAI models", "meta": "AI & ML · / · simonwillison.net"},
    {"url": "https://inkwell.coze.com/article/art_xjk6m9", "title": "datasette-agent-micropython 0.1a0", "meta": "AI & ML · / · simonwillison.net"},
    {"url": "https://inkwell.coze.com/article/art_e52rpq", "title": "micropython-wasm 0.1a1", "meta": "AI & ML · / · simonwillison.net"},
    {"url": "https://inkwell.coze.com/article/art_gjni8i", "title": "An Ode to the Exacting Pedantry of Computers", "meta": "Web & Design · / · blog.jim-nielsen.com"},
    {"url": "https://inkwell.coze.com/article/art_dxhlir", "title": "California Brown Pelican", "meta": "AI & ML · / · simonwillison.net"},
    {"url": "https://inkwell.coze.com/article/art_wdy2rr", "title": "GitHub's plan for Agents — Kyle Daigle, GitHub", "meta": "AI & ML · / · Latent Space"},
    {"url": "https://inkwell.coze.com/article/art_yrxth0", "title": "Logic for Programmers extra credits", "meta": "Programming · / · buttondown.com/hillelwayne"},
    {"url": "https://inkwell.coze.com/article/art_l8px4d", "title": "AI Doesn't Have ROI", "meta": "Tech Culture · / · wheresyoured.at · · · Ed Zitron"},
    {"url": "https://inkwell.coze.com/article/art_o4m5x", "title": "Rotation revisited: Another unidirectional algorithm", "meta": "Systems · / · devblogs.microsoft.com/oldnewthing · · · Raymond Chen"},
    {"url": "https://inkwell.coze.com/article/art_wrre4f", "title": "Using FourSquare's API to post location checkins to social media", "meta": "Tech Culture · / · shkspr.mobi · · · @edent"},
    {"url": "https://inkwell.coze.com/article/art_d49oem", "title": "People are too big to fit inside our heads", "meta": "Indie · / · Henrik Karlsson · · · Henrik Karlsson"},
    {"url": "https://inkwell.coze.com/article/art_q6bsbi", "title": "Pluralistic: The tedious power of storytelling (02 Jun 2026) must-we-pretend", "meta": "Tech Culture · / · pluralistic.net · · · Cory Doctorow"},
]

def parse_meta(meta_str):
    """解析 meta 字符串，提取分类和来源"""
    parts = [p.strip() for p in meta_str.split('·')]
    category = parts[0] if len(parts) > 0 else ''
    source = parts[2] if len(parts) > 2 else ''
    return category, source

def main():
    result = []
    for art in ARTICLES_DATA:
        category, source = parse_meta(art['meta'])
        result.append({
            'title': art['title'],
            'url': art['url'],
            'inkwell_url': art['url'],
            'category': category,
            'source': source,
        })
    
    output = Path('./inkwell-archive/data/20260604_articles.json')
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"保存了 {len(result)} 篇文章到 {output}")

if __name__ == "__main__":
    from pathlib import Path
    main()
