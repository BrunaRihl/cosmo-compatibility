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
    header()
    print("Welcome to the CosmoCompatibility Zodiac Traits Test!\nThis program will calculate the percentage of traits you share in common with your zodiac sign.")

def menu():
    print("\nChoose one of the following options:")
    print("1: Would you like more information about what zodiac signs are?")
    print("2: Do you want to start the test?")
    print("3: Exit the program")

    while True:
        option = int(input("\nPlease enter one of the options: "))
        if option in [1, 2, 3]:
            return option

        print("Incorrect value entered. Please try again.")

def main():
    header()
    # TODO: add validation day e month
    day = int(input("Enter the day of your birth (1-31): "))
    month = int(input("Enter the month of your birth (1-12): "))
    
    sign = get_sign(day, month)
    sign = sign.lower()

    initial_screen()
    play = menu()
    while True:
        if play == 1:
            play = menu()

        if play == 2:
            play = menu()

        if play == 3:
            break   
    

main()


