
## getting started: import libraries
import pandas as pd
import os
import matplotlib as plt
import requests
import numpy as np
import json

## introduction message 
print('Welcome, you can get information about countries, languages and currency here!')
print('''
            Press 1 for information about a country
            Press 2 to obtain a list of countries by language
            Press 3 to obtain a list of countries by currency
            Press 4 to exit      ''')
## start search
while True:
    try:
        user_input = int(input("To start your search, enter an integer from 1 to 4:"))
        if user_input == 1:
            country_code = input('Enter cca2, ccn3, cca3 or cioc country code:')
            url = f'https://restcountries.com/v3.1/alpha/{country_code}'
            response = requests.get(url)
            if response.status_code == 200:
                country_data = response.json()
                country_name = [country["name"] for country in country_data]
                print(f"Country name {country_name}:")
                country_cap = [country["capital"] for country in country_data]
                print(f"Capital: {country_cap}")
                lang = [country["languages"] for country in country_data]
                print(f"Languages: {lang}")
                curr = [country["currencies"] for country in country_data]
                print(f"Currencies: {curr}")
                call = [country["idd"] for country in country_data]
                print(f"Calling code: {call}")
                pop = [country["population"] for country in country_data]
                print(f"Population: {pop}")
                reg = [country["region"] for country in country_data]
                print(f"Region: {reg}")
            else:
                print("Sorry, this country is not in our database") 
        elif user_input == 2:
            language = input('Enter ISO 639-2 language code:')
            url = f'https://restcountries.com/v3.1/lang/{language}'
            response = requests.get(url)
            if response.status_code == 200:
                country_data = response.json()
                print(f"Countries speaking {language}:")
                for country in country_data:
                    print(country['name']['common'])
                    print("------------------------")
            else:
                print("Sorry, this language code is not valid") 
        elif user_input == 3:
            currency_code = input('Enter currency:')
            response = requests.get(f"https://restcountries.com/v3.1/currency/{currency_code}")
            if response.status_code == 200:
                c_data = response.json()
                print(f"Countries using {currency_code}:") #reformat
                for country in c_data:
                    print(country['name']['common'])
                    print("------------------------")
            else:
                print("Sorry, this currency code is not valid")
        elif user_input == 4:
            print('Thank you for using our program')
    except ValueError:
        print("That was not an integer. Please try again.")

