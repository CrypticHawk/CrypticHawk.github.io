# scripts/scrape_deals.py

import json

# TODO: Replace this with real web scraping or API calls later!
def fetch_deals():
    # Each deal: product, store, price, affiliate_url, category
    return [
        {
            "product": "Lenovo Legion Slim 5",
            "store": "Takealot",
            "price": 27999,
            "affiliate_url": "https://afflink.com/lenovo-legion-takealot",
            "category": "Laptops"
        },
        {
            "product": "Lenovo Legion Slim 5",
            "store": "Loot",
            "price": 28999,
            "affiliate_url": "https://afflink.com/lenovo-legion-loot",
            "category": "Laptops"
        },
        {
            "product": "Xbox Series S",
            "store": "Incredible Connection",
            "price": 6499,
            "affiliate_url": "https://afflink.com/xbox-series-s-incredible",
            "category": "Consoles"
        },
        {
            "product": "Xbox Series S",
            "store": "Takealot",
            "price": 6199,
            "affiliate_url": "https://afflink.com/xbox-series-s-takealot",
            "category": "Consoles"
        }
        # ... add more sample deals here or scrape for real!
    ]

def best_deals_by_product(deals):
    """Return only the lowest price offer for each product."""
    best = {}
    for d in deals:
        pname = d["product"]
        if pname not in best or d["price"] < best[pname]["price"]:
            best[pname] = d
    # Attach list of ALL offers for "show more"
    for d in deals:
        pname = d["product"]
        best.setdefault(pname, {}).setdefault("alternatives", []).append(d)
    return list(best.values())

if __name__ == "__main__":
    all_deals = fetch_deals()
    best_deals = best_deals_by_product(all_deals)
    # Write all deals (for show-more) and best deals to a JSON file
    with open("deals.json", "w", encoding="utf-8") as f:
        json.dump({
            "all_deals": all_deals,
            "best_deals": best_deals
        }, f, indent=2)
    print("Generated deals.json!")
