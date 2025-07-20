import json

# Dummy deals for demonstration.
takealot = [
    {
        "product": "Demo Laptop",
        "store": "Takealot",
        "price": 9999,
        "affiliate_url": "https://www.takealot.com",
        "category": "Laptops"
    }
]
loot = [
    {
        "product": "Demo Laptop",
        "store": "Loot",
        "price": 10499,
        "affiliate_url": "https://www.loot.co.za",
        "category": "Laptops"
    }
]
evetech = []
ic = []
mania = []

def master_deal_merge(*deal_lists):
    all_deals = [deal for sublist in deal_lists for deal in sublist]
    best = {}
    for d in all_deals:
        pname = d["product"]
        if pname not in best or d["price"] < best[pname]["price"]:
            best[pname] = d
    for d in all_deals:
        pname = d["product"]
        best.setdefault(pname, {}).setdefault("alternatives", []).append(d)
    return list(best.values()), all_deals

if __name__ == "__main__":
    print("SCRIPT IS RUNNING")
    best_deals, all_deals = master_deal_merge(takealot, loot, evetech, ic, mania)
    with open('deals.json', 'w', encoding='utf-8') as f:
        json.dump({
            "best_deals": best_deals,
            "all_deals": all_deals
        }, f, indent=2)
    print(f"Scraped and saved {len(best_deals)} best deals, {len(all_deals)} total offers.")
