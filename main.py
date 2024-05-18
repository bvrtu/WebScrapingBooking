import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk # To more customizable GUI
from ttkbootstrap.widgets import DateEntry # To calendar
from tkinter import messagebox # To give error messages
import locale # To price converting
import os # To reach file
from datetime import datetime # To check the date format


class HotelScraper:


    # Checking internet connection

    def check_internet_connection(self):
        try:
            requests.get("https://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False

    # Web Scraping Function

    def scrape_hotels(self, city, date1, date2):

        # Error condition if user can't reach to Internet

        if not self.check_internet_connection():
            messagebox.showerror("Error", "No internet connection available.")
            return
        try:
            if city == "Rome":
                url = "https://www.booking.com/searchresults.html?ss=Rome%2C+Lazio%2C+Italy&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-126693&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=68f06406a62e018b&ac_meta=GhA5MzJkNjQwYzI3ODQwMDQwIAAoATICZW46BHJvbWVAAEoAUAA%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
            elif city == "Barcelona":
                url = "https://www.booking.com/searchresults.html?ss=Barcelona%2C+Catalonia%2C+Spain&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-372490&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=1ecb654f2a0201c9&ac_meta=GhBkZmJlNjU2ZDQwYjgwMzI2IAAoATICZW46CWJhcmNlbG9uYUAASgBQAA%3D%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
            elif city == "Paris":
                url = "https://www.booking.com/searchresults.html?ss=Paris%2C+Ile+de+France%2C+France&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-1456928&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=5a1c6547c8b503ed&ac_meta=GhA0N2FkNjU0ZWZiYjYwMzI3IAAoATICZW46BXBhcmlzQABKAFAA&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
            elif city == "Berlin":
                url = "https://www.booking.com/searchresults.html?ss=Berlin%2C+Berlin+Federal+State%2C+Germany&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-1746443&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=b2cb652eee2e0712&ac_meta=GhBjMGI1NjUzZTA2M2UwMTViIAAoATICZW46BmJlcmxpbkAASgBQAA%3D%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
            elif city == "London":
                url = "https://www.booking.com/searchresults.html?ss=London%2C+Greater+London%2C+United+Kingdom&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-2601889&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=649964ae8d98025f&ac_meta=GhBmYzBlNjRiZjgyYWEwMjVlIAAoATICZW46BmxvbmRvbkAASgBQAA%3D%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
            elif city == "Vienna":
                url = "https://www.booking.com/searchresults.html?ss=Vienna%2C+Vienna+%28state%29%2C+Austria&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-1995499&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=c85664a1e65a01a7&ac_meta=GhBkOWQyNjRhZDA3ZTQwMjI4IAAoATICZW46BnZpZW5uYUAASgBQAA%3D%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
            elif city == "Brussels":
                url = "https://www.booking.com/searchresults.html?ss=Brussels%2C+Brussels+Region%2C+Belgium&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-1955538&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=4ad451e0f8d6005c&ac_meta=GhA4ZDExNTFlNmI2NjIwMDYzIAAoATICZW46CGJydXNzZWxzQABKAFAA&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
            elif city == "Amsterdam":
                url = "https://www.booking.com/searchresults.html?ss=Amsterdam%2C+Noord-Holland%2C+Netherlands&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-2140479&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=c6dc6484bb650445&ac_meta=GhBiM2M5NjQ5MWZiNWMwMGNmIAAoATICZW46CWFtc3RlcmRhbUAASgBQAA%3D%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
            elif city == "Zurich":
                url = "https://www.booking.com/searchresults.html?ss=Z%C3%BCrich%2C+Canton+of+Zurich%2C+Switzerland&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-2554935&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=d57b640de50301d5&ac_meta=GhAyYzQ1NjQ2M2JjMGIwMTAwIAAoATICZW46Bnp1cmljaEAASgBQAA%3D%3D&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"
            elif city == "Budapest":
                url = "https://www.booking.com/searchresults.html?ss=Budapest%2C+Pest%2C+Hungary&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-850553&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=3d1b651b22ea018e&ac_meta=GhBlMDViNjUxZjBlOGYwMDQxIAAoATICZW46CGJ1ZGFwZXN0QABKAFAA&checkin="+date1+"&checkout="+date2+"&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR"

            print(url)

            headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/51.0.2704.64 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'}

            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            hotels = soup.find_all('div', {"data-testid": "property-card"})
            hotels_data = []

            rating_type = ""
            counter = 0

            for hotel in hotels:
            # To scrape first 10 hotels

                if counter == 10:
                    break

                name_element = hotel.find('div', {'data-testid': 'title'})
                name = name_element.text.strip()

                rating_element = hotel.find("a", {"data-testid": "secondary-review-score-link"})

                # Scraping the rating with type

                if rating_element is not None:
                    rating_text = rating_element['aria-label'] # In HTML it looks like "aria-label = Comfort: Scored 8.9". I'm taking the aria-label and splitting into type and rating.
                    split_text = rating_text.split(": ")
                    rating_type = split_text[0]
                    rating = split_text[1].split()[1]
                    rating = float(rating)
                else:
                    rating_type = "Not Given"
                    rating = "Not Given"

                address_element = hotel.find("span", {"data-testid": "address"})
                if address_element is not None:
                    address = address_element.text.strip()
                else:
                    address = "Not Given"

                distance_element = hotel.find("span", {"data-testid": "distance"})
                if distance_element is not None:
                    distance = distance_element.text.strip()
                else:
                    distance = "Not Given"

                price_element = hotel.find("span", {"data-testid": "price-and-discounted-price"})
                if price_element is not None:
                    price = price_element.text.strip()
                else:
                    price = "Not Given"

                # Appending the list with scraped datas

                hotels_data.append({'Hotel Name': name, "Address": address, "Distance": distance,"Type and Rating": rating_type + "\n" + str(rating), "Price": price})

                counter += 1

            # Sorting based on ratings

            def sort_by_rating(x):
                rating = x['Type and Rating'].split('\n')[1]
                if rating == 'Not Given':
                    return float('-inf') # Sending not givens at the end of the list
                else:
                    return float(rating)

            hotels_data.sort(key=sort_by_rating, reverse=True)

            hotels = pd.DataFrame(hotels_data)
            hotels.head()
            hotels.to_csv('myhotels.csv', header=True, index=False)

        # Request error handling
        except requests.Timeout:
            messagebox.showerror("Error", "Request timed out. Please check your internet connection.")
            return

        except requests.RequestException as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")
            return


class GUI:
    def __init__(self):
        self.currency = None

    def gui(self):
        check_in_date = ""
        check_out_date = ""
        city_string = ""
        self.last_search = {"city": "", "check_in_date": "", "check_out_date": "", "currency": None}

        # Checking date format
        def check_date_format(date_string):
            try:
                # Date formatting
                datetime.strptime(date_string, '%m/%d/%y')
                return True
            except ValueError:
                return False

        # A function to take dates from calendar and turn them into correct string form to eject in url

        def get_dates():
            nonlocal check_in_date, check_out_date
            check_in_date = calendar1.entry.get()
            check_out_date = calendar2.entry.get()

            if not check_date_format(check_in_date) or not check_date_format(check_out_date):
                messagebox.showerror("Error", "Invalid date format. Please use mm/dd/yy format.")
                return

            start_date = datetime.strptime(check_in_date, "%m/%d/%y").date()
            end_date = datetime.strptime(check_out_date, "%m/%d/%y").date()
            today_date = datetime.today().date()
            date_difference_days = (end_date - start_date).days
            date_difference_days_2 = (end_date - start_date).days

            if date_difference_days > 90:
                messagebox.showerror("Error", "You cannot have more than 90 days between check-in and check-out dates.")
                return

            if date_difference_days_2 <= 0:
                messagebox.showerror("Error", "Check-out date cannot be before or same as check-in date.")
                return

            if start_date < today_date:
                messagebox.showerror("Error", "Check-in date cannot be before today.")
                return

            f_check_in_date = check_in_date.split("/") # mm/dd/yy to "mm", "dd", "yy"
            f_check_out_date = check_out_date.split("/")
            check_in_date = "20" + f_check_in_date[2] + "-" + f_check_in_date[0] + "-" + f_check_in_date[1] # Turning the date into appropriate URL format
            check_out_date = "20" + f_check_out_date[2] + "-" + f_check_out_date[0] + "-" + f_check_out_date[1] # In URL yyyy-mm-dd

            update_search_button_state()

        # Getting city from dropdown list

        def get_city(event):
            nonlocal city_string
            city_string = combobox.get()

            if city_string:
                button2.config(state="normal")
            else:
                button2.config(state="disabled")

        # Converting the currency

        def convert_to_euro(price_tl):
            tl_to_euro_rate = 0.0333333  # TL to Euro conversion rate (1 TL = 0.0333333 Euro)
            price_tl = price_tl.replace('TL', '').strip()  # Remove TL and any leading/trailing whitespace
            price_euro = round(float(price_tl) * tl_to_euro_rate, 2)
            return f"{price_euro} €"

        def convert_to_tl(price_euro):
            euro_to_tl_rate = 30  # Euro to TL conversion rate (1 Euro = 30 TL)

            # Set locale for the correct interpretation of decimal numbers
            locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')  # Assuming English locale

            # Remove '€' and any leading/trailing whitespace
            price_euro = price_euro.replace('€', '').strip()

            # Convert to float and apply conversion rate
            price_tl = round(locale.atof(price_euro) * euro_to_tl_rate, 2)

            return f"{price_tl} TL"

        def euro_clicked():
            self.currency = "euro"

        # This two function returning the currency to Euro or TL when radiobutton is pressed

        def tl_clicked():
            self.currency = "tl"

        # Creating and updating the treeview
        def create_and_update_treeview():

            hotels_data = pd.read_csv('myhotels.csv')

            # Returning the table into dynamic form. (If the user makes a search the table changes on GUI.)
            for child in hotelframe.winfo_children():
                if isinstance(child, ttk.Treeview):
                    child.destroy()

            custom_style = ttk.Style()
            custom_style.configure("Custom.Treeview", rowheight=85)

            tree = ttk.Treeview(hotelframe, style="Custom.Treeview")
            tree["columns"] = ("Hotel Name", "Address", "Distance", "Type and Rating", "Price")

            tree.column("#0", width=0)  # Hidden column
            tree.column("Hotel Name", anchor=tk.W,width=300)
            tree.column("Address", anchor=tk.W,width=300)
            tree.column("Distance", anchor=tk.W,width=300)
            tree.column("Type and Rating", anchor=tk.W,width=300)
            tree.column("Price", anchor=tk.W,width=300)

            tree.heading("#0", text="", anchor=tk.W)
            tree.heading("Hotel Name", text="Hotel Name", anchor=tk.W)
            tree.heading("Address", text="Address", anchor=tk.W)
            tree.heading("Distance", text="Distance", anchor=tk.W)
            tree.heading("Type and Rating", text="Type and Rating", anchor=tk.W)
            tree.heading("Price", text="Price", anchor=tk.W)

            for index, row in hotels_data.head(5).iterrows():
                tree.insert("", index, values=(row['Hotel Name'], row['Address'], row['Distance'], row['Type and Rating'], row['Price']))

            tree.pack()

        # When you press the "Find Your Hotel!" button this function works.

        def searchfunc(city,date1,date2):

            # Price conversion if block. (If user do not changes the city and the dates it means just it is price converting)
            if self.last_search["city"] == city and self.last_search["check_in_date"] == date1 and self.last_search["check_out_date"] == date2:
                if self.last_search["currency"] != self.currency:
                    if self.currency == "tl":
                        hotels_data = pd.read_csv('myhotels.csv')
                        for index, row in hotels_data.iterrows():
                            hotels_data.at[index, 'Price'] = convert_to_tl(row['Price'])
                        hotels_data.to_csv('myhotels.csv', header=True, index=False)

                        create_and_update_treeview()

                        messagebox.showinfo("Info", "Currency conversion applied.")

                        self.last_search["currency"] = self.currency

                    elif self.currency == "euro":
                        hotels_data = pd.read_csv('myhotels.csv')
                        for index, row in hotels_data.iterrows():
                            hotels_data.at[index, 'Price'] = convert_to_euro(row['Price'])
                        hotels_data.to_csv('myhotels.csv', header=True, index=False)

                        create_and_update_treeview()

                        messagebox.showinfo("Info", "Currency conversion applied.")

                        self.last_search["currency"] = self.currency


                else: # If user changes nothing from the last search (city + dates + price currency)
                    messagebox.showinfo("Warning", "You haven't changed any values from your last search.")
                return

            self.last_search["city"] = city
            self.last_search["check_in_date"] = date1
            self.last_search["check_out_date"] = date2
            self.last_search["currency"] = self.currency

            global currency

            # These 3 if blocks are controlling the is the city selected, is the currency selected and is the date selected.

            if not date1 or not date2:
                messagebox.showerror("Error", "Please select check-in and check-out dates.")
                return

            if not city:
                messagebox.showerror("Error", "Please select a city.")
                return

            if not self.currency:
                messagebox.showerror("Error", "Please select a currency type.")
                return

            scraper = HotelScraper()
            scraper.scrape_hotels(city_string, check_in_date, check_out_date)

            hotels_data = pd.read_csv('myhotels.csv')

            # While scraping I take the prices as euro on default. If user selects tl this function returns euro prices to TL prices.

            if self.currency == "tl":
                for index, row in hotels_data.iterrows():
                    hotels_data.at[index, 'Price'] = convert_to_tl(row['Price'])

                # Writes on csv file
                hotels_data.to_csv('myhotels.csv', header=True, index=False)

            create_and_update_treeview()

            self.last_search["city"] = city
            self.last_search["check_in_date"] = date1
            self.last_search["check_out_date"] = date2
            self.last_search["currency"] = self.currency

            create_and_update_treeview()


        # Window

        window = ttk.Window(themename="vapor")
        window.title("Find Your Hotel")
        window.state("zoomed")

        # First mainframe to select city,currency and dates

        mainframe = ttk.Frame(window,width=2000,height=400,borderwidth=10, relief="groove")
        mainframe.pack_propagate(False)
        mainframe.pack()

        # First subframe to choose the city

        frame1 = ttk.Frame(mainframe, width=300, height=200, borderwidth=10, relief="groove")
        frame1.pack_propagate(False)
        frame1.place(x=200,y=50)

        city_label = ttk.Label(frame1, text="Choose a city from the list.")
        city_label.pack()

        items = ("Rome", "Barcelona", "Paris", "Berlin", "London", "Vienna", "Brussels", "Amsterdam", "Zurich", "Budapest")
        comboboxString = tk.StringVar()
        combobox = ttk.Combobox(frame1, state="readonly", width=10, height=5, textvariable=comboboxString)
        combobox["values"] = items
        combobox.pack()

        city_label2 = ttk.Label(frame1, text="Selected City:")
        city_label2.place(x=68, y=150)

        city_label3 = ttk.Label(frame1,textvariable=comboboxString)
        city_label3.place(x=155, y=150)

        combobox.bind("<<ComboboxSelected>>", get_city)

        # Second subframe to select check-in and out dates

        frame2 = ttk.Frame(mainframe, width=300, height=200, borderwidth=10, relief="groove")
        frame2.pack_propagate(False)
        frame2.place(x=550, y=50)

        label1 = ttk.Label(frame2, text="Check-in Date")
        label1.pack()

        calendar1 = DateEntry(frame2)
        calendar1.pack(pady=5)

        label2 = ttk.Label(frame2, text="Check-out Date")
        label2.pack(pady=5)

        calendar2 = DateEntry(frame2)
        calendar2.pack()

        button = ttk.Button(frame2, text="Select Dates", command=get_dates, bootstyle = "secondary")
        button.pack(pady=14)

        # Third subframe to searching button

        frame3 = ttk.Frame(mainframe)
        frame3.place(x=645, y=300)

        button2 = ttk.Button(frame3, text="Find Your Hotel!", command=lambda: searchfunc(city_string, check_in_date, check_out_date), bootstyle = "success", state="disabled")
        button2.pack()

        # Fourth subframe to pick currency

        frame4 = ttk.Frame(mainframe,width=300, height=200, borderwidth=10, relief="groove")
        frame4.pack_propagate(False)
        frame4.place(x=900, y=50)

        label4 = ttk.Label(frame4, text="Price Currency")
        label4.pack()

        radiobutton = ttk.Radiobutton(frame4, text="Euro",value=1, command=euro_clicked)
        radiobutton.pack(pady=40)
        radiobutton2 = ttk.Radiobutton(frame4, text="TL", value=2, command=tl_clicked)
        radiobutton2.pack()

        # Second mainframe to display the tree

        hotelframe = ttk.Frame(window, width=2000, height=500, borderwidth=10, relief="groove")
        hotelframe.pack()

        def update_search_button_state():
            if city_string and check_in_date and check_out_date and self.currency:
                button2.config(state="enabled")
            else:
                button2.config(state="disabled")

        combobox.bind("<<ComboboxSelected>>", lambda event: (get_city(event), update_search_button_state()))
        calendar1.bind("<<DateEntrySelected>>", lambda event: (get_dates(), update_search_button_state()))
        calendar2.bind("<<DateEntrySelected>>", lambda event: (get_dates(), update_search_button_state()))
        radiobutton.config(command=lambda: (euro_clicked(), update_search_button_state()))
        radiobutton2.config(command=lambda: (tl_clicked(), update_search_button_state()))

        window.mainloop()


def main():
    app = GUI()
    app.gui()

if __name__ == "__main__":
    main()