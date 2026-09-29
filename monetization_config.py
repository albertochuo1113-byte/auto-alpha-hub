# 變現設定中心（未來申請到 ID 後直接改這裡，全站自動生效）
ADSENSE_CLIENT_ID = ""  # 例如: "ca-pub-1234567890123456"
AMAZON_AFFILIATE_TAG = ""  # 例如: "alberto-20"
GUMROAD_PRODUCT_URL = "https://gumroad.com"  # 你的數位資產或推薦工具庫

# 預留的廣告與贊助 HTML 模組
def get_monetization_footer():
    html = f"""
    <div style="margin-top: 40px; padding: 20px; background-color: #f8fafc; border-radius: 8px; border: 1px solid #e2e8f0;">
        <h4 style="margin-top:0;">⚡ 精選推薦與贊助</h4>
        <p style="font-size: 0.95rem; color: #475569;">
            本站由 Hermes Agent 全自動化運作。探索我們的 
            <a href="{GUMROAD_PRODUCT_URL}" target="_blank" style="color: #2563eb; font-weight: bold;">[極簡風控與自動化第二大腦工具箱]</a>。
        </p>
    </div>
    """
    if ADSENSE_CLIENT_ID:
        html += f"""
        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT_ID}" crossorigin="anonymous"></script>
        """
    return html
