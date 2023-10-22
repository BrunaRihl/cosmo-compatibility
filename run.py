from data import data, signs
import datetime
import pyfiglet
import os



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


def about_screen():
    clear()
    header()
    print("""Zodiac signs are part of astrology, 
    which is a belief system that suggests a connection 
    between the positions and movements of celestial bodies 
    (such as planets and stars) and events and characteristics on Earth, 
    including human personality and behavior.""")
    print("The zodiac is divided into twelve signs, each associated with specific dates of the year. They are: Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, and Pisces.")
    print("It is believed that each sign has its own set of characteristics, strengths, weaknesses, and compatibility with other signs. Remember that astrology is a belief system and is not based on empirical scientific evidence.")


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_sign(zodiac_sign):
    print(f'{"Your zodiac sign is " + zodiac_sign.upper():^60}')
    print("\n\n")


def test_screen(sign):
    clear()
    header()
    print_sign(sign)

        for num, record in enumerate(data):
        question = record["question"]
        all_options = record["answer"]
        options = build_options(all_options.copy(), sign)


def main():
    clear()
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
            about_screen()
            play = menu()

        if play == 2:
            play = menu()

        if play == 3:
            break   
    

main()


