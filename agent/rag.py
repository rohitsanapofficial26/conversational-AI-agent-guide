import json

with open("data/knowledge_base.json") as f:
    KB = json.load(f)

def get_pricing_info():
    basic = KB["pricing"]["basic"]
    pro = KB["pricing"]["pro"]

    return f"""
Basic Plan:
- {basic['price']}
- {basic['videos']}
- {basic['resolution']}

Pro Plan:
- {pro['price']}
- {pro['videos']}
- {pro['resolution']}
- Features: {', '.join(pro['features'])}
"""

