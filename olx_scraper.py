pip install beautifulsoup4 requests

import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.olx.in/items/q-car-cover"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Find all listing cards (this may need updates if OLX changes layout)
items = soup.find_all("li", class_="EIR5N")  # OLX often uses this class for listings

results = []

for item in items:
    title_tag = item.find("span", class_="_2tW1I")
    loc_tag = item.find("span", class_="tjgMj")
    price_tag = item.find("span", class_="_89yzn")

    title = title_tag.text.strip() if title_tag else "N/A"
    location = loc_tag.text.strip() if loc_tag else "N/A"
    price = price_tag.text.strip() if price_tag else "N/A"

    results.append([title, location, price])

# Save to CSV
with open("olx_car_cover_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Location", "Price"])
    writer.writerows(results)

print("Saved results to olx_car_cover_results.csv")
