import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.widgets import DateEntry


class HotelScraper:
    def scrape_hotels(self, city, date1, date2):

        if (city == "Rome"):
            url = "https://www.booking.com/searchresults.html?ss=Rome%2C+Lazio%2C+Italy&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-126693&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=68f06406a62e018b&ac_meta=GhA5MzJkNjQwYzI3ODQwMDQwIAAoATICZW46BHJvbWVAAEoAUAA%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
        elif (city == "Barcelona"):
            url = "https://www.booking.com/searchresults.html?ss=Barcelona%2C+Catalonia%2C+Spain&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-372490&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=1ecb654f2a0201c9&ac_meta=GhBkZmJlNjU2ZDQwYjgwMzI2IAAoATICZW46CWJhcmNlbG9uYUAASgBQAA%3D%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
        elif (city == "Paris"):
            url = "https://www.booking.com/searchresults.html?ss=Paris%2C+Ile+de+France%2C+France&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-1456928&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=5a1c6547c8b503ed&ac_meta=GhA0N2FkNjU0ZWZiYjYwMzI3IAAoATICZW46BXBhcmlzQABKAFAA&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
        elif (city == "Berlin"):
            url = "https://www.booking.com/searchresults.html?ss=Berlin%2C+Berlin+Federal+State%2C+Germany&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-1746443&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=b2cb652eee2e0712&ac_meta=GhBjMGI1NjUzZTA2M2UwMTViIAAoATICZW46BmJlcmxpbkAASgBQAA%3D%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
        elif (city == "London"):
            url = "https://www.booking.com/searchresults.html?ss=London%2C+Greater+London%2C+United+Kingdom&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-2601889&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=649964ae8d98025f&ac_meta=GhBmYzBlNjRiZjgyYWEwMjVlIAAoATICZW46BmxvbmRvbkAASgBQAA%3D%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
        elif (city == "Vienna"):
            url = "https://www.booking.com/searchresults.html?ss=Vienna%2C+Vienna+%28state%29%2C+Austria&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-1995499&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=c85664a1e65a01a7&ac_meta=GhBkOWQyNjRhZDA3ZTQwMjI4IAAoATICZW46BnZpZW5uYUAASgBQAA%3D%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
        elif (city == "Brussels"):
            url = "https://www.booking.com/searchresults.html?ss=Brussels%2C+Brussels+Region%2C+Belgium&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-1955538&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=4ad451e0f8d6005c&ac_meta=GhA4ZDExNTFlNmI2NjIwMDYzIAAoATICZW46CGJydXNzZWxzQABKAFAA&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
        elif (city == "Amsterdam"):
            url = "https://www.booking.com/searchresults.html?ss=Amsterdam%2C+Noord-Holland%2C+Netherlands&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-2140479&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=c6dc6484bb650445&ac_meta=GhBiM2M5NjQ5MWZiNWMwMGNmIAAoATICZW46CWFtc3RlcmRhbUAASgBQAA%3D%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
        elif (city == "Zurich"):
            url = "https://www.booking.com/searchresults.html?ss=Z%C3%BCrich%2C+Canton+of+Zurich%2C+Switzerland&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-2554935&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=d57b640de50301d5&ac_meta=GhAyYzQ1NjQ2M2JjMGIwMTAwIAAoATICZW46Bnp1cmljaEAASgBQAA%3D%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
        elif (city == "Budapest"):
            url = "https://www.booking.com/searchresults.html?ss=Budapest%2C+Pest%2C+Hungary&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-850553&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=3d1b651b22ea018e&ac_meta=GhBlMDViNjUxZjBlOGYwMDQxIAAoATICZW46CGJ1ZGFwZXN0QABKAFAA&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"

        print(url)

        headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/51.0.2704.64 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'}

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        hotels = soup.find_all('div', {"data-testid": "property-card"})
        hotels_data = []

        rating_type = ""
        counter = 0;

        for hotel in hotels:
            if counter == 10:
                break;

            name_element = hotel.find('div', {'data-testid': 'title'})
            name = name_element.text.strip()

            rating_element = hotel.find("span", {"class": "a3332d346a"})
            if (rating_element is not None):
                rating_type = rating_element.text.strip().split()[0]
                rating = rating_element.text.strip().split()[1]
            else:
                rating_element = hotel.find("div", {"class": "a3b8729ab1 d86cee9b25"})
                rating_type = "Not Given"
                rating = rating_element.text.strip().split()[1]

            address_element = hotel.find("span", {"data-testid": "address"})
            address = address_element.text.strip()

            distance_element = hotel.find("span", {"data-testid": "distance"})
            distance = distance_element.text.strip()

            price_element = hotel.find("span", {"data-testid": "price-and-discounted-price"})
            price = price_element.text.strip()

            hotels_data.append({'Hotel Name': name, "Address": address, "Distance": distance,
                                'Type and Rating': rating_type + "\n" + rating, "Price": price})

            counter += 1

        #hotels_data.sort(key=lambda x: float(x['Type and Rating'].split('\n')[1]), reverse=True)

        hotels = pd.DataFrame(hotels_data)
        hotels.head()
        hotels.to_csv('myhotels.csv', header=True, index=False)


class GUI:
    def __init__(self, master):
        self.master = master

    def gui(self):
        check_in_date = ""
        check_out_date = ""
        city_string = ""

        def get_dates():
            nonlocal check_in_date, check_out_date
            check_in_date = calendar1.entry.get()
            check_out_date = calendar2.entry.get()
            f_check_in_date = check_in_date.split("/")
            f_check_out_date = check_out_date.split("/")
            check_in_date = "20" + f_check_in_date[2] + "-" + f_check_in_date[0] + "-" + f_check_in_date[1]
            check_out_date = "20" + f_check_out_date[2] + "-" + f_check_out_date[0] + "-" + f_check_out_date[1]

        def get_city(event):
            nonlocal city_string
            city_string = combobox.get()

        def searchfunc(city,date1,date2):
            scraper = HotelScraper()
            scraper.scrape_hotels(city_string, check_in_date, check_out_date)

        # window
        window = ttk.Window(themename="darkly")
        window.title("Find Your Hotel")
        window.state("zoomed")

        # first frame to choose city
        frame1 = ttk.Frame(window, width=500, height=250, borderwidth=10, relief="groove")
        frame1.pack_propagate(False)
        frame1.place(x=0, y=0, anchor="nw")

        city_label = ttk.Label(frame1, text="Choose a city from the list.")
        city_label.pack()

        items = ("Rome", "Barcelona", "Paris", "Berlin", "London", "Vienna", "Brussels", "Amsterdam", "Zurich", "Budapest")
        comboboxString = tk.StringVar(value=items[0])
        combobox = ttk.Combobox(frame1, state="readonly", width=10, height=5, textvariable=comboboxString)
        combobox["values"] = items
        combobox.pack()

        combobox.bind("<<ComboboxSelected>>", get_city)

        # second frame to select check-in and out dates
        frame2 = ttk.Frame(window, width=500, height=250, borderwidth=10, relief="groove")
        frame2.pack_propagate(False)
        frame2.place(relx=1.0, y=0, anchor="ne")

        label1 = ttk.Label(frame2, text="Check-in Date")
        label1.pack()

        calendar1 = DateEntry(frame2)
        calendar1.pack()

        label2 = ttk.Label(frame2, text="Check-out Date")
        label2.pack()

        calendar2 = DateEntry(frame2)
        calendar2.pack(pady=10)

        button = ttk.Button(frame2, text="OK", command=get_dates)
        button.pack()

        frame3 = ttk.Frame(window, width=500, height=250, borderwidth=10, relief="groove")
        frame3.pack_propagate(False)
        frame3.pack(side = "bottom")

        label3 = ttk.Label(frame3, text="Search")
        label3.pack()

        button2 = ttk.Button(frame3, text="Search",command=lambda: searchfunc(city_string,check_in_date,check_out_date))
        button2.pack()

        window.mainloop()


def main():
    root = tk.Tk()
    app = GUI(root)
    app.gui()


if __name__ == "__main__":
    main()
