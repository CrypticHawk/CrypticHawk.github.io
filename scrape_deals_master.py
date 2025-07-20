import json
import os

print("SCRIPT IS RUNNING!")
print("CWD:", os.getcwd())
print("Files in CWD:", os.listdir())

# Dummy deals for test (works even if scraping is empty)
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
    print("About to merge deals...")
    best_deals, all_deals = master_deal_merge(takealot, loot, evetech, ic, mania)
    print("Best deals:", len(best_deals), "All deals:", len(all_deals))
