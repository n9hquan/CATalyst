"""
Project's Title: CATalyst
Name: Nguyen Chinh Quan
Github username: n9hquan
edX username: Remonn_302
City, Country: Ho Chi Minh City, Viet Nam
Recorded date: 12 Aug 2024
"""
import cowsay
import requests
import webbrowser
import textwrap
import sys
from pprint import pprint

def main():
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    while True:
        mode = int(input("Select one of these options below:\n1. Get a random cat fact\n2. Customize a random cat picture\n3. Learn about a specific cat breed\n4. Exit the program.\n"))
        if mode == 1:
            cowsay.meow(random_cat_fact())
            break
        elif mode == 2:
            make_your_own_cat()
            break
        elif mode == 3:
            cat_information()
            break
        elif mode == 4:
            print("Thank you for using our CATalyst engine!")
            sys.exit()
    main()

def random_cat_fact():
    fact_url = "https://meowfacts.herokuapp.com/"
    fact_response = requests.get(fact_url).json()['data'][0]
    return fact_response

def make_your_own_cat():
    phrase = input("What do you want to write in the picture? ")
    phrase = phrase.replace(" ", "%20")
    while True:
        font_size = input("How big is the font? ")
        try:
            if font_size.isnumeric():
                break
            elif not font_size.isnumeric():
                raise Exception("Input is not a number type! Please type again.")
        except Exception as e:
            print(e)
    while True:
        font_color = input("Finally, please choose the color for the font: ")
        try:
            if font_color.isalpha():
                break
            elif not font_color.isalpha():
                raise Exception("Input is not a word type! Please type again.")
        except Exception as e:
            print(e)
    cat_generator_url = f"https://cataas.com/cat/says/{phrase}?fontSize={font_size}&fontColor={font_color}"
    # Case insensitive for font color
    # Default color is black
    webbrowser.open(cat_generator_url)
    return


def cat_information():
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url).json()
    names = []
    for i in range(len(response)):
        names.append(response[i]["name"])
    print("Here is a list of cat breeds:")
    pprint(names)
    while True:
        user_sort = input("Do you want to filter the breeds out via the first capital letter? ").lower()
        try:
            if user_sort not in ["n","no","y","yes"]:
                raise Exception("Invalid input! Please answer 'yes' or 'no'.")
            elif user_sort in ['n','no']:
                while True:
                    breed = input("What cat breed do you want to read about? ").lower().title()
                    if breed in names:
                        break
                for i in range(len(response)):
                    if response[i]["name"] == breed:
                        wrapped_description = textwrap.fill(response[i]["description"], width=80, initial_indent = "  ", subsequent_indent="  ")
                        print(f"Description:\n{wrapped_description}")
                        print(f"Life span: {response[i]["life_span"]}")
                        break
                return
            else:
                while True:
                    capital_letter = input("Please type in the first letter you want to filter out: ").upper()
                    if len(capital_letter) == 1 and capital_letter.isalpha():
                        sorted_list = []
                        if len(sorted_list) == 0:
                            for name in names:
                                if name.startswith(capital_letter):
                                    sorted_list.append(name)
                            print(f"Here is a list of cat breeds that starts with {capital_letter}: ")
                            pprint(sorted_list)
                            break
                        else:
                            print(f"No cat breed starts with the letter {capital_letter}!")
                while True:
                    breed = input("What cat breed do you want to read about? ").lower().title()
                    if breed in sorted_list:
                        break
                for i in range(len(response)):
                    if response[i]["name"] == breed:
                        wrapped_description = textwrap.fill(response[i]["description"], width=80, initial_indent = "  ", subsequent_indent="  ")
                        print(f"Description:\n{wrapped_description}")
                        print(f"Life span: {response[i]["life_span"]}")
                        break
                return
        except Exception as e:
            print(e)


if __name__ == "__main__":
    print("Welcome to our CATalyst engine!")
    main()
