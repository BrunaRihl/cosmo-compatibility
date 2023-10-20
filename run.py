from data import signs
import datetime
import pyfiglet

def get_current_year():
    today = datetime.date.today()
    return  today.year


def get_sign(day, month):
    year = get_current_year()
    birthday = datetime.date(year, month, day)
    
    for sign in signs:
        period = signs[sign]
        if period["start"] <= birthday <= period["end"]:
            return sign
    return "Invalid month or day"


def initial_screen():
    font = pyfiglet.Figlet()
    message = "Cosmo * Compatibility"
    rendered_message = font.renderText(message)
    print(rendered_message)
    print("Welcome to the CosmoCompatibility Zodiac Traits Test!\nThis program will calculate the percentage of traits you share in common with your zodiac sign.")
    while True:
        play_test = str(input('Do you want to start the test? (y/n): '))
        if play_test in 'yYnN':
            return play_test


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


