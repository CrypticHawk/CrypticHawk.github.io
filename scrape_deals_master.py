import json
import requests
from bs4 import BeautifulSoup
import os
import time

print("SCRIPT IS RUNNING!")
print("CWD:", os.getcwd())
print("Files in CWD:", os.listdir())

########## --- SCRAPER FUNCTIONS --- ##########

# --- Takealot ---
def scrape_takealot_laptops():
    print("Scraping Takealot laptops...")
    url = "https://www.takealot.com/all?filter=Category:Laptops"
    headers = {"User-Agent": "Mozilla/5.0"}
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
    print("Takealot laptops found:", len(deals))
    return deals

def scrape_takealot_phones():
    print("Scraping Takealot phones...")
    url = "https://www.takealot.com/all?filter=Category:Cellphones"
    headers = {"User-Agent": "Mozilla/5.0"}
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
                "category": "Phones"
            })
    print("Takealot phones found:", len(deals))
    return deals

def scrape_takealot_consoles():
    print("Scraping Takealot consoles...")
    url = "https://www.takealot.com/all?filter=Category:Gaming-Consoles"
    headers = {"User-Agent": "Mozilla/5.0"}
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
                "category": "Consoles"
            })
    print("Takealot consoles found:", len(deals))
    return deals

# --- Loot ---
def scrape_loot_laptops():
    print("Scraping Loot laptops...")
    url = "https://www.loot.co.za/category/laptops"
    deals = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.select(".product-list-item"):
        name = item.select_one(".product-title")
        price = item.select_one(".price")
        link = item.select_one("a")
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                "product": product,
                "store": "Loot",
                "price": price_int,
                "affiliate_url": "https://www.loot.co.za" + link['href'],
                "category": "Laptops"
            })
    print("Loot laptops found:", len(deals))
    return deals

def scrape_loot_phones():
    print("Scraping Loot phones...")
    url = "https://www.loot.co.za/category/cellphones"
    deals = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.select(".product-list-item"):
        name = item.select_one(".product-title")
        price = item.select_one(".price")
        link = item.select_one("a")
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                "product": product,
                "store": "Loot",
                "price": price_int,
                "affiliate_url": "https://www.loot.co.za" + link['href'],
                "category": "Phones"
            })
    print("Loot phones found:", len(deals))
    return deals

def scrape_loot_consoles():
    print("Scraping Loot consoles...")
    url = "https://www.loot.co.za/category/game-consoles"
    deals = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.select(".product-list-item"):
        name = item.select_one(".product-title")
        price = item.select_one(".price")
        link = item.select_one("a")
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                "product": product,
                "store": "Loot",
                "price": price_int,
                "affiliate_url": "https://www.loot.co.za" + link['href'],
                "category": "Consoles"
            })
    print("Loot consoles found:", len(deals))
    return deals

# --- Evetech ---
def scrape_evetech_laptops():
    print("Scraping Evetech laptops...")
    url = "https://www.evetech.co.za/laptops-for-sale-south-africa.aspx"
    deals = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.select(".item-list .item"):
        name = item.select_one(".item-title")
        price = item.select_one(".item-price")
        link = item.select_one("a")
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                "product": product,
                "store": "Evetech",
                "price": price_int,
                "affiliate_url": "https://www.evetech.co.za" + link['href'],
                "category": "Laptops"
            })
    print("Evetech laptops found:", len(deals))
    return deals

def scrape_evetech_consoles():
    print("Scraping Evetech consoles...")
    url = "https://www.evetech.co.za/game-consoles-for-sale-south-africa.aspx"
    deals = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.select(".item-list .item"):
        name = item.select_one(".item-title")
        price = item.select_one(".item-price")
        link = item.select_one("a")
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                "product": product,
                "store": "Evetech",
                "price": price_int,
                "affiliate_url": "https://www.evetech.co.za" + link['href'],
                "category": "Consoles"
            })
    print("Evetech consoles found:", len(deals))
    return deals

# --- Incredible Connection ---
def scrape_incredible_connection_laptops():
    print("Scraping Incredible Connection laptops...")
    url = "https://www.incredible.co.za/laptops"
    deals = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.select(".product-item-info"):
        name = item.select_one(".product-item-link")
        price = item.select_one(".price")
        link = item.select_one(".product-item-link")
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                "product": product,
                "store": "Incredible Connection",
                "price": price_int,
                "affiliate_url": link['href'],
                "category": "Laptops"
            })
    print("IC laptops found:", len(deals))
    return deals

def scrape_incredible_connection_phones():
    print("Scraping Incredible Connection phones...")
    url = "https://www.incredible.co.za/cellphones"
    deals = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.select(".product-item-info"):
        name = item.select_one(".product-item-link")
        price = item.select_one(".price")
        link = item.select_one(".product-item-link")
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                "product": product,
                "store": "Incredible Connection",
                "price": price_int,
                "affiliate_url": link['href'],
                "category": "Phones"
            })
    print("IC phones found:", len(deals))
    return deals

def scrape_incredible_connection_consoles():
    print("Scraping Incredible Connection consoles...")
    url = "https://www.incredible.co.za/gaming-consoles"
    deals = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.select(".product-item-info"):
        name = item.select_one(".product-item-link")
        price = item.select_one(".price")
        link = item.select_one(".product-item-link")
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                "product": product,
                "store": "Incredible Connection",
                "price": price_int,
                "affiliate_url": link['href'],
                "category": "Consoles"
            })
    print("IC consoles found:", len(deals))
    return deals

# --- Computer Mania ---
def scrape_computer_mania_laptops():
    print("Scraping Computer Mania laptops...")
    url = "https://computermania.co.za/collections/laptops"
    deals = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.select(".product-card"):
        name = item.select_one(".product-card__title")
        price = item.select_one(".price__regular")
        link = item.select_one("a")
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                "product": product,
                "store": "Computer Mania",
                "price": price_int,
                "affiliate_url": "https://computermania.co.za" + link['href'],
                "category": "Laptops"
            })
    print("Computer Mania laptops found:", len(deals))
    return deals

def scrape_computer_mania_phones():
    print("Scraping Computer Mania phones...")
    url = "https://computermania.co.za/collections/mobile-phones"
    deals = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.select(".product-card"):
        name = item.select_one(".product-card__title")
        price = item.select_one(".price__regular")
        link = item.select_one("a")
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                "product": product,
                "store": "Computer Mania",
                "price": price_int,
                "affiliate_url": "https://computermania.co.za" + link['href'],
                "category": "Phones"
            })
    print("Computer Mania phones found:", len(deals))
    return deals

def scrape_computer_mania_consoles():
    print("Scraping Computer Mania consoles...")
    url = "https://computermania.co.za/collections/gaming-consoles"
    deals = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.select(".product-card"):
        name = item.select_one(".product-card__title")
        price = item.select_one(".price__regular")
        link = item.select_one("a")
        if name and price and link:
            product = name.text.strip()
            price_clean = ''.join(filter(str.isdigit, price.text))
            price_int = int(price_clean) if price_clean else 0
            deals.append({
                "product": product,
                "store": "Computer Mania",
                "price": price_int,
                "affiliate_url": "https://computermania.co.za" + link['href'],
                "category": "Consoles"
            })
    print("Computer Mania consoles found:", len(deals))
    return deals

########## --- MERGE & MAIN --- ##########

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
    print("About to scrape all deals...")
    # Laptops
    takealot_laptops = scrape_takealot_laptops()
    time.sleep(1)
    loot_laptops = scrape_loot_laptops()
    time.sleep(1)
    evetech_laptops = scrape_evetech_laptops()
    time.sleep(1)
    ic_laptops = scrape_incredible_connection_laptops()
    time.sleep(1)
    mania_laptops = scrape_computer_mania_laptops()
    time.sleep(1)
    # Phones
    takealot_phones = scrape_takealot_phones()
    time.sleep(1)
    loot_phones = scrape_loot_phones()
    time.sleep(1)
    ic_phones = scrape_incredible_connection_phones()
    time.sleep(1)
    mania_phones = scrape_computer_mania_phones()
    time.sleep(1)
    # Consoles
    takealot_consoles = scrape_takealot_consoles()
    time.sleep(1)
    loot_consoles = scrape_loot_consoles()
    time.sleep(1)
    evetech_consoles = scrape_evetech_consoles()
    time.sleep(1)
    ic_consoles = scrape_incredible_connection_consoles()
    time.sleep(1)
    mania_consoles = scrape_computer_mania_consoles()
    time.sleep(1)

    best_deals, all_deals = master_deal_merge(
        takealot_laptops, loot_laptops, evetech_laptops, ic_laptops, mania_laptops,
        takealot_phones, loot_phones, ic_phones, mania_phones,
        takealot_consoles, loot_consoles, evetech_consoles, ic_consoles, mania_consoles
    )
    print("Best deals:", len(best_deals), "All deals:", len(all_deals))
    with open('deals.json', 'w', encoding='utf-8') as f:
        json.dump({
            "best_deals": best_deals,
            "all_deals": all_deals
        }, f, indent=2)
    print("WROTE JSON!")
