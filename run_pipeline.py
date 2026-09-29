import os, sys, json, datetime, urllib.request

# 設定利基主題庫（自營交易風控、AI自動化、數位遊民生產力）
TOPICS = [
    "Prop Firm 交易風控與 3% 硬止損策略詳解",
    "Mac Mini M4 部署本地 AI Agent 的極致被動收入工作流",
    "數位遊民如何用 Obsidian 與第二大腦打造一人公司",
    "FTMO 與 The5ers 考核規則比對與避坑指南",
    "自動化 Micro-SaaS 的極簡架構與變現模式"
]

import random
selected_topic = random.choice(TOPICS)
today_str = datetime.datetime.now().strftime("%Y-%m-%d")
filename = f"posts/{today_str}-{random.randint(100,999)}.md"

os.makedirs("posts", exist_ok=True)

# 寫入 Markdown 文章模板
article_content = f"""---
title: "{selected_topic}"
date: {today_str}
tags: [Trading, AI, Productivity, SecondBrain]
---

# {selected_topic}

> 本文由 Hermes Agent 依據最新行業洞察與演算法全自動蒸餾產出。

## 核心痛點分析
在當前的數位競爭環境中，如何達成高槓桿、低摩擦的運作是所有獨立創作者與交易者的首要挑戰...

## 具體執行框架 (Actionable Framework)
1. **確立邊界**：嚴格執行風險阻斷機制。
2. **自動化沉澱**：將日常繁複流程固化為腳本或模板。
3. **長期複利**：讓代碼與數位資產 24 小時為你工作。

---
*贊助推薦 / 推薦工具：[查看極簡風控與 AI 自動化工具箱](https://github.com)*
"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(article_content)

print(f"SUCCESS: Article generated -> {filename}")
