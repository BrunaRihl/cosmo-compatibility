import random
import datetime
import os

from dateutil.relativedelta import relativedelta
from tqdm import tqdm

from data import data, signs, sign_description
try:
    from auth import update_worksheet
except Exception as e:
    print("Unable to connect to the internet: ", e)


def get_year():
    """
    Returns the year for calculations.
    This function provides a way to use the datetime module independently of the
    system's actual year.
    """
    return 2023


def get_sign(day, month):
    """
    Determines the zodiac sign based on the provided day and month.
    Args:
        day (int): The day of birth.
        month (int): The month of birth.
    Returns the zodiac sign associated with the date, or "Invalid month or day"
    if the input is invalid.
    """
    year = get_year()
    birthday = datetime.date(year, month, day)
    
    for sign in signs:
        period = signs[sign]
        if period["start"].month > period["end"].month:
            period["end"] = period["end"] + relativedelta(years=1) 
    
        if period["start"] <= birthday <= period["end"]:
            return sign
    
    return "Invalid month or day"


def header():
    """
    ASCII art initial screen.
    """
    cosmo_message = """
▒█▀▀█ █▀▀█ █▀▀ █▀▄▀█ █▀▀█ 　
▒█░░░ █░░█ ▀▀█ █░▀░█ █░░█ 　
▒█▄▄█ ▀▀▀▀ ▀▀▀ ▀░░░▀ ▀▀▀▀ 　 
▒█▀▀█ █▀▀█ █▀▄▀█ █▀▀█ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀▄ ░▀░ █░░ ░▀░ ▀▀█▀▀ █░░█
▒█░░░ █░░█ █░▀░█ █░░█ █▄▄█ ░░█░░ ▀█▀ █▀▀▄ ▀█▀ █░░ ▀█▀ ░░█░░ █▄▄█
▒█▄▄█ ▀▀▀▀ ▀░░░▀ █▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀░ ▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ ▄▄▄█ 
"""

    print(cosmo_message)


def initial_screen():
    """
    Displays the initial screen with program introduction.
    Clears the screen, displays the program header, and provides
    a welcome message along with an introduction to the purpose of the program.
    """
    clear()
    header()
    print("Welcome to the CosmoCompatibility Zodiac Traits Test!")
    print("This program will calculate the percentage of traits you") 
    print("share in common with your zodiac sign.")


def menu():
    """
    Displays the menu and prompts the user to choose an option.
    """

    print("\nChoose one of the following options:")
    print("1: More information about what zodiac signs are")
    print("2: Start the test")
    print("3: Exit program")

    while True:
        try:
            option = int(input("\nPlease enter one of the options: "))
            if option in [1, 2, 3]:
                return choose_screen(option)

            print(f"Invalid option. Please choose between 1 and 3.")
        except ValueError:
            print(f"Invalid option. Please choose between 1 and 3.")

            continue


def about_screen():
    """
    Clears the screen, displays the program header, and displays 
    information about zodiac signs.
    """

    clear()
    print("""
    Zodiac signs are part of astrology, which is a belief system that 
    suggests a connection between the positions and movements of celestial
    bodies (such as planets and stars) and events and characteristics on Earth,
    including human personality and behavior.\n
    The zodiac is divided into twelve signs, each associated with specific dates
    of the year. They are: Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, 
    Scorpio, Sagittarius, Capricorn, Aquarius, and Pisces.\n
    It is believed that each sign has its own set of characteristics, strengths, 
    weaknesses, and compatibility with other signs. Remember that astrology is a
    belief system and is not based on empirical scientific evidence.
    """)


def clear():
    """
    This function checks the operating system and uses the appropriate command
    to clears the terminal screen.
    """

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_sign(zodiac_sign):
    """
    Prints the user's zodiac sign.
    Args:
        zodiac_sign (str): The user's zodiac sign.
    """
    print(f'{"Your zodiac sign is " + zodiac_sign.upper():^60}')
    print("\n\n")


def print_instructions():
    print("Instructions:")
    print("Choose the option that best aligns with your personality.")
    print("If your choice matches the personality description of your zodiac sign,")
    print("the compatibility progress bar will increase")
    print("There are four options (1, 2, 3, 4). Type your choice and press 'Enter'\n")


def shuffle_data(s_data):
    """
    Shuffles a list of data.
    Args:
        s_data (list): The data to be shuffled.
    Returns list: The shuffled data.
    """
    random.shuffle(s_data)
    return s_data


def shuffle_answers(answers):
    """
    Randomly selects a zodiac sign from a dictionary of answers.
    Args:
        answers (dict): A dictionary of zodiac signs and their corresponding answers.
    Returns str: A randomly selected zodiac sign.
    """
    signs = list(answers.keys())
    return signs[random.randint(1, len(signs)-1)]


def build_options(answers, sign):
    """
    Builds a list of options for a zodiac sign.
    Args:
        answers (dict): A dictionary of zodiac signs and their corresponding answers.
        sign (str): The zodiac sign for which options are being built.
    Returns a list of options, including the correct answer.
    """
    show = [{sign: answers.pop(sign)}]
    for _ in range(1,4):  
        index = shuffle_answers(answers)
        chosen_option = answers.pop(index)
        show.append({index: chosen_option})
        
    return show


def test_screen(sign):
    """    
    Conducts the Zodiac Traits Test for a specific zodiac sign.
    This function initiates the test, presents questions and options to the user, 
    evaluates the user's responses, and calculates an affinity score based on correct 
    answers. It also displays a progress bar to track the affinity test progress.
    Args:
        sign (str): The zodiac sign for which the test is conducted (user zodiac sign).
    """
    clear()
    print_sign(sign)
    print_instructions()
    affinity_score = 0
    data_shuffled = shuffle_data(data)

    with tqdm(total=len(data_shuffled), ncols=60, bar_format='Compatibility:|{bar}|{percentage:3.0f}%') as pbar:
        for num, record in enumerate(data_shuffled):
            question = record["question"]
            all_options = record["answer"]
            options = build_options(all_options.copy(), sign)
            shuffled_options = shuffle_data(options)
            
            # To assemble the question
            print(f"\n\n{question}")  
            for n, option in enumerate(shuffled_options, 1):
                answer = list(option.values())[0]
                print(f"{n}: {answer}")

            # The user's input/response   
            while True:
                try:     
                    answer = int(input("\nEnter an answer: "))
                    answer = options[answer - 1]
                except IndexError:
                    print('invalid option. Try between 1 and 4')
                    continue
                except ValueError:
                    print('invalid option. Try between 1 and 4')
                    continue
                break
            clear()
            print_sign(sign)

            # "Correct" or "Incorrect"
            if list(answer.keys())[0] == sign:
                affinity_score += 1
                pbar.update(1)
            
            pbar.set_postfix(current=num + 1)

        return affinity_score


def result_screen(sign, result):
    """
    Displays the zodiac sign description and result.
    Args:
        sign (str): The zodiac sign of the user.
        result (int): The affinity score indicating the number of correct answers.
    """
    
    print("""
    Test complete!  This is your final result! \n    Thank you for completing the compatibility test!

Remember, a persons personality is influenced by a variety
of factors beyond their sun sign, such as the positions of other planets 
in their birth chart.This test was created for fun and entertainment, 
not as an exact science. The traits associated with each sign are generalizations. 
Enjoy it in a relaxed manner!\n""")

    print(f"    A brief description about your zodiac sign:{sign_description[sign]}")

    try:
        worksheet = update_worksheet(sign, result)
        draw_progressbar(worksheet)
    except Exception as e:
        print("Unable to connect to the internet: ", e)


def draw_progressbar(worksheet):
    """
    Draws a progress bar for visualizing data from the given worksheet.
    This function takes a worksheet as input and visualizes progress data using a progress bar.
    Each zodiac sign is aligned uniformly within the progress bar by adding spaces at the end.
    Args:
        worksheet (list): A list of rows containing data to be visualized.
    """

    format = ':|{bar}|{percentage:3.0f}%'
    word_len_max = 15
    for num, row in enumerate(worksheet):
        if num == 0:
            continue

        # Added a space at the end of each sign to align them in the same space.
        # Example:
        # sagittarius 11 characters + 5 white space = 15
        # aries 5 characters + 10 white space = 15
        space = " " * (word_len_max - len(row[0]))
        sign = row[0] + space

        with tqdm(total=100, ncols=60, bar_format=sign + format) as pbar:
            pbar.update(int(float(row[3])))
 

def choose_screen(menu_id):
    """
    Takes a menu choice and executes the corresponding action.
    Args:
        menu_id (int): The ID of the chosen menu option.
    Returns: int: The menu option chosen.
    """
    match menu_id:
        case 1:
            about_screen()

        case 2:
            clear()
            while True:
                try:   
                    month = int(input("Enter the month of your birth (1-12): "))
                    day = int(input("Enter the day of your birth (1-31): "))

                    if month == 2 and day == 29:
                        day = 28
                    datetime.date(get_year(), month, day)
                except ValueError:
                    print("Invalid data. Please try again.")
                    continue

                break

            sign = get_sign(day, month)
            sign = sign.lower()
            print_sign(sign)
            result = test_screen(sign)
            result_screen(sign, result)

        case 3:
            clear()
            print("\nThank you for exploring CosmoCompatibility!")
            print("Have a great day and see you next time!\n")


    return menu_id


def main():
    """
    Prompts the user for their birthdate and conducts the test.
    Runs the main program logic for the Zodiac Traits Test.
    """
    initial_screen()

    while True:
        result = menu()
        if result == 3:
            break
  
main()

