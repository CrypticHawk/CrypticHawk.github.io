import json
import requests
from bs4 import BeautifulSoup
import os

print("SCRIPT IS RUNNING!")
print("CWD:", os.getcwd())
print("Files in CWD:", os.listdir())

def scrape_takealot_laptops():
    url = "https://www.takealot.com/all?filter=Category:Laptops"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    deals = []
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.select(".product-card"):
        name = item.select_one(".product-title")
        price = item.select_one(".currency")
        link = item.select_one("a")
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                "product": product,
                "store": "Takealot",
                "price": price_int,
                "affiliate_url": "https://www.takealot.com" + link['href'],
                "category": "Laptops"
            })
    print("Takealot deals found:", len(deals))
    return deals

# Dummy data for other stores (replace with real scraping code later)
loot = []
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
    for pname, best_deal in best.items():
        best_deal["alternatives"] = [
            d for d in all_deals if d["product"] == pname and d is not best_deal
        ]
    return list(best.values()), all_deals

if __name__ == "__main__":
    print("About to scrape deals...")
    takealot = scrape_takealot_laptops()
    best_deals, all_deals = master_deal_merge(takealot, loot, evetech, ic, mania)
    print("Best deals:", len(best_deals), "All deals:", len(all_deals))
    with open('deals.json', 'w', encoding='utf-8') as f:
        json.dump({
            "best_deals": best_deals,
            "all_deals": all_deals
        }, f, indent=2)
    print("WROTE JSON!")
