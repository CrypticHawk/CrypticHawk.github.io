import requests
from bs4 import BeautifulSoup
import json

def scrape_takealot_laptops():
    print("Scraping Takealot...")
    deals = []
    headers = {"User-Agent": "Mozilla/5.0"}
    url = 'https://www.takealot.com/all?filter=Category:Laptops'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
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
                'affiliate_url': f"https://www.takealot.com{link['href']}",
                'category': 'Laptops'
            })
    return deals

def scrape_loot_laptops():
    print("Scraping Loot...")
    deals = []
    url = "https://www.loot.co.za/category/laptops"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for item in soup.select('.product-list-item'):
        name = item.select_one('.product-title')
        price = item.select_one('.price')
        link = item.select_one('a')
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                'product': product,
                'store': 'Loot',
                'price': price_int,
                'affiliate_url': f"https://www.loot.co.za{link['href']}",
                'category': 'Laptops'
            })
    return deals

def scrape_evetech_laptops():
    print("Scraping Evetech...")
    deals = []
    url = "https://www.evetech.co.za/laptops-for-sale-south-africa.aspx"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for item in soup.select('.item-list .item'):
        name = item.select_one('.item-title')
        price = item.select_one('.item-price')
        link = item.select_one('a')
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                'product': product,
                'store': 'Evetech',
                'price': price_int,
                'affiliate_url': f"https://www.evetech.co.za{link['href']}",
                'category': 'Laptops'
            })
    return deals

def scrape_incredible_connection_laptops():
    print("Scraping Incredible Connection...")
    deals = []
    url = "https://www.incredible.co.za/laptops"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for item in soup.select('.product-item-info'):
        name = item.select_one('.product-item-link')
        price = item.select_one('.price')
        link = item.select_one('.product-item-link')
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                'product': product,
                'store': 'Incredible Connection',
                'price': price_int,
                'affiliate_url': link['href'],
                'category': 'Laptops'
            })
    return deals

def scrape_computer_mania_laptops():
    print("Scraping Computer Mania...")
    deals = []
    url = "https://computermania.co.za/collections/laptops"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for item in soup.select('.product-card'):
        name = item.select_one('.product-card__title')
        price = item.select_one('.price__regular')
        link = item.select_one('a')
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                'product': product,
                'store': 'Computer Mania',
                'price': price_int,
                'affiliate_url': f"https://computermania.co.za{link['href']}",
                'category': 'Laptops'
            })
    return deals

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
    takealot = scrape_takealot_laptops()
    loot = scrape_loot_laptops()
    evetech = scrape_evetech_laptops()
    ic = scrape_incredible_connection_laptops()
    mania = scrape_computer_mania_laptops()
    best_deals, all_deals = master_deal_merge(takealot, loot, evetech, ic, mania)
    with open('deals.json', 'w', encoding='utf-8') as f:
        json.dump({
            "best_deals": best_deals,
            "all_deals": all_deals
        }, f, indent=2)
    print(f"Scraped and saved {len(best_deals)} best deals, {len(all_deals)} total offers.")
