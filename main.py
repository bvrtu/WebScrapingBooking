import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.booking.com/searchresults.html?ss=Rome&ssne=Rome&ssne_untouched=Rome&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-126693&dest_type=city&checkin=2024-06-03&checkout=2024-06-16&group_adults=2&no_rooms=1&group_children=0"
headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/51.0.2704.64 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
hotels = soup.find_all('div', {"data-testid":"property-card"})
hotels_data = []

for hotel in hotels:

    name_element = hotel.find('div', {'data-testid': 'title'})
    rating_element = hotel.find("div", {"class": "a3b8729ab1 d86cee9b25"})
    address_element = hotel.find("span", {"data-testid":"address"})
    distance_element = hotel.find("span", {"data-testid": "distance"})
    price_element = hotel.find("span", {"class": "f6431b446c fbfd7c1165 e84eb96b1f"})

    name = name_element.text.strip()
    rating = rating_element.text.strip().split()
    address = address_element.text.strip()
    distance = distance_element.text.strip()
    price = price_element.text.strip()

    hotels_data.append({'Hotel Name': name,"Address": address, "Distance": distance, 'Rating': rating[1], "Price": price})

hotels_data = hotels_data[:10]

hotels_data.sort(key=lambda x: x['Rating'], reverse=True)

hotels = pd.DataFrame(hotels_data)
hotels.head()
hotels.to_csv('myhotels.csv', header=True, index=False)