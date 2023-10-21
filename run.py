from data import data, signs
import datetime
import pyfiglet


def get_year():
    # solution to use datetime independent of the current year
    return 2023


def get_sign(day, month):
    year = get_year()
    birthday = datetime.date(year, month, day)
    
    for sign in signs:
        period = signs[sign]
        if period["start"] <= birthday <= period["end"]:
            return sign
    
    return "Invalid month or day"

def header():
    font = pyfiglet.Figlet()
    message = "Cosmo * Compatibility"
    rendered_message = font.renderText(message)
    print(rendered_message)


def initial_screen():
    clear()
    header()
    print("Welcome to the CosmoCompatibility Zodiac Traits Test!\nThis program will calculate the percentage of traits you share in common with your zodiac sign.")


def main():
    play = initial_screen()
    if play in 'Yy':
        while True:
            day = int(input("Enter the day of your birth (1-31): "))
            month = int(input("Enter the month of your birth (1-12): "))

            sign = get_sign(day, month)
            sign = sign.lower()
            print(f"Your zodiac sign is {sign}")
        break


main()


