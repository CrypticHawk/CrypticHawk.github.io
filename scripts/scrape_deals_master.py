if __name__ == "__main__":
    takealot = [
        {
            "product": "Demo Laptop",
            "store": "Takealot",
            "price": 9999,
            "affiliate_url": "https://www.takealot.com",
            "category": "Laptops"
        }
    ]
    loot = []
    evetech = []
    ic = []
    mania = []
    best_deals, all_deals = master_deal_merge(takealot, loot, evetech, ic, mania)
    with open('deals.json', 'w', encoding='utf-8') as f:
        json.dump({
            "best_deals": best_deals,
            "all_deals": all_deals
        }, f, indent=2)
    print(f"Scraped and saved {len(best_deals)} best deals, {len(all_deals)} total offers.")
