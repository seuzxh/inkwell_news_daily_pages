#!/usr/bin/env python3
"""获取 InkWell 文章详情"""

import json
import re
import time
from pathlib import Path

# 文章列表（从浏览器提取的24篇文章）
ARTICLES = [
    {"url": "https://inkwell.coze.com/article/art_p28uzh", "title": "Is datacentre sovereignty really that important?", "category": "Indie"},
    {"url": "https://inkwell.coze.com/article/art_pvdd2g", "title": "Now that your newsletter is AI-generated, I've Unsubscribed", "category": "Indie"},
    {"url": "https://inkwell.coze.com/article/art_strk50", "title": "🔬Scaling Past Informal AI - Carina Hong, Axiom Math", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_dj3gbf", "title": "⚡️Satya Nadella: No Priors x Latent Space Crossover Special at Microsoft Build", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_vrdx5c", "title": "Naively summing an alternating series", "category": "Essays"},
    {"url": "https://inkwell.coze.com/article/art_rjaiwy", "title": "Skills Registry Threat Models", "category": "Indie"},
    {"url": "https://inkwell.coze.com/article/art_l7qxm2", "title": "Uber Caps Usage of AI Tools Like Claude Code to Manage Costs", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_p3lwi4", "title": "London Data Store Relaunch", "category": "Tech Culture"},
    {"url": "https://inkwell.coze.com/article/art_qs26xv", "title": "Quoting Natalie Lung", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_h9prfw", "title": "[AINews] Microsoft Build: MAI-Thinking-1 and MAI Family models", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_jfdhoz", "title": "Welcoming the Philippine Government to Have I Been Pwned", "category": "Security"},
    {"url": "https://inkwell.coze.com/article/art_y3zgdt", "title": "A survey of inlining heuristics", "category": "Programming"},
    {"url": "https://inkwell.coze.com/article/art_bpaodo", "title": "Microsoft's new MAI models", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_xjk6m9", "title": "datasette-agent-micropython 0.1a0", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_e52rpq", "title": "micropython-wasm 0.1a1", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_gjni8i", "title": "An Ode to the Exacting Pedantry of Computers", "category": "Web & Design"},
    {"url": "https://inkwell.coze.com/article/art_dxhlir", "title": "California Brown Pelican", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_wdy2rr", "title": "GitHub's plan for Agents — Kyle Daigle, GitHub", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_yrxth0", "title": "Logic for Programmers extra credits", "category": "Programming"},
    {"url": "https://inkwell.coze.com/article/art_l8px4d", "title": "AI Doesn't Have ROI", "category": "Tech Culture"},
    {"url": "https://inkwell.coze.com/article/art_o4m5x", "title": "Rotation revisited: Another unidirectional algorithm", "category": "Systems"},
    {"url": "https://inkwell.coze.com/article/art_wrre4f", "title": "Using FourSquare's API to post location checkins to social media", "category": "Tech Culture"},
    {"url": "https://inkwell.coze.com/article/art_d49oem", "title": "People are too big to fit inside our heads", "category": "Indie"},
    {"url": "https://inkwell.coze.com/article/art_q6bsbi", "title": "Pluralistic: The tedious power of storytelling (02 Jun 2026) must-we-pretend", "category": "Tech Culture"},
]

# trending 文章
TRENDING = [
    {"url": "https://inkwell.coze.com/article/art_i49th5", "title": "Microsoft Copilot Cowork Exfiltrates Files", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_oh5rat", "title": "The mysterious Hy3 LLM is topping OpenRouter Model Rankings by a large margin", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_inst3c", "title": "The pressure", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_l1536i", "title": "Hackers Simply Asked Meta AI to Give Them Access to High-Profile Instagram Accounts. It Worked", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_bbz3jw", "title": "Why Video Agent models are next — Ethan He, xAI Grok Imagine", "category": "AI & ML"},
    {"url": "https://inkwell.coze.com/article/art_xo92nc", "title": "Revenge of The Business Idiot", "category": "Tech Culture"},
]

def main():
    # 合并所有文章
    all_articles = ARTICLES + TRENDING
    
    # 去重
    seen = set()
    unique = []
    for a in all_articles:
        if a['url'] not in seen:
            seen.add(a['url'])
            unique.append(a)
    
    print(f"总共 {len(unique)} 篇文章")
    
    # 保存到文件
    output = Path("./inkwell-archive/data/20260604_raw.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(unique, f, ensure_ascii=False, indent=2)
    
    print(f"已保存到 {output}")

if __name__ == "__main__":
    main()
