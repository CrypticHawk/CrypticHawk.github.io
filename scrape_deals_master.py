import requests
from bs4 import BeautifulSoup
import json

def scrape_takealot_laptops():
    # -- Adjust the URL or add more category URLs for Takealot here
    url = 'https://www.takealot.com/all?filter=Category:Laptops'
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    deals = []
    for item in soup.select('.product-card'):
        name = item.select_one('.product-title')
        price = item.select_one('.currency')
        link = item.select_one('a')
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                'product': product,
                'store': 'Takealot',
                'price': price_int,
                'affiliate_url': f"https://www.takealot.com{link['href']}",  # Replace with your affiliate logic if needed
                'category': 'Laptops'
            })
    return deals

def scrape_loot_laptops():
    # --- Placeholder: Add Loot scraping logic or similar categories here.
    return []

def scrape_incredible_connection_laptops():
    # --- Placeholder: Add IC scraping logic here.
    return []

def scrape_evetech_laptops():
    # --- Placeholder: Add Evetech scraping logic here.
    return []

def scrape_computer_mania_laptops():
    # --- Placeholder: Add Computer Mania scraping logic here.
    return []

def master_deal_merge(*deal_lists):
    all_deals = [deal for sublist in deal_lists for deal in sublist]
    best = {}
    for d in all_deals:
        pname = d["product"]
        if pname not in best or d["price"] < best[pname]["price"]:
            best[pname] = d
    # Attach alternatives (all offers for each product)
    for d in all_deals:
        pname = d["product"]
        best.setdefault(pname, {}).setdefault("alternatives", []).append(d)
    return list(best.values()), all_deals

if __name__ == "__main__":
    takealot = scrape_takealot_laptops()
    loot = scrape_loot_laptops()
    ic = scrape_incredible_connection_laptops()
    evetech = scrape_evetech_laptops()
    mania = scrape_computer_mania_laptops()
    best_deals, all_deals = master_deal_merge(takealot, loot, ic, evetech, mania)
    with open('deals.json', 'w', encoding='utf-8') as f:
        json.dump({
            "best_deals": best_deals,
            "all_deals": all_deals
        }, f, indent=2)
    print(f"Scraped and saved {len(best_deals)} best deals, {len(all_deals)} total offers.")
