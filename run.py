import random
import datetime

from dateutil.relativedelta import relativedelta
from tqdm import tqdm
from data import data, signs, sign_description

try:
    from auth import update_worksheet, get_worksheet
except Exception as e:
    print("Unable to connect to the internet: ", e)


def get_year():
    """
    Returns the year for calculations.
    This function provides a way to use the datetime module
    independently of the system's actual year.
    """
    return 2023


def get_sign(day, month):
    """
    Determines the zodiac sign based on the provided day and month.
    Args:
        day (int): The day of birth.
        month (int): The month of birth.
    """
    year = get_year()
    birthday = datetime.date(year, month, day)

    # Check if the birth date falls within the transition dates
    # between Capricorn and Aquarius
    if datetime.date(year, 1, 1) <= birthday <= datetime.date(year, 1, 19):
        return "Capricorn"
    else:
        # Loop through the signs to determine the correct sign
        for sign in signs:
            period = signs[sign]
            # Check if the start of the period is in a different year than
            # the end (e.g., December to January)
            if period["start"].month > period["end"].month:
                period["end"] = period["end"] + relativedelta(years=1)
            # Check if the birth date is within the period for the current sign
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
    print("share in common with your zodiac sign.\n")


def menu():
    """
    Displays the menu and prompts the user to choose an option.
    """

    print("--- Zodiac Compatibility Test Menu ---")
    print("1. Learn more about Zodiac Signs")
    print("2. Start the Compatibility Test")
    print("3. View Compatibility Percentages")
    print("4. Exit Program")

    while True:
        try:
            option = int(input("\nPlease enter one of the options: "))
            if option in [1, 2, 3, 4]:
                return choose_screen(option)

            print(f"Invalid option. Please choose between 1 and 4.")
        except ValueError:
            print(f"Invalid option. Please choose between 1 and 4.")

            continue


def about_screen():
    """
    Clears the screen, displays the program header, and displays
    information about zodiac signs.
    """
    clear()
    print(
        """
Zodiac signs are part of astrology, which is a belief system that
suggests a connection between the positions and movements of celestial
bodies (such as planets and stars) and events and characteristics on Earth,
including human personality and behavior.\n
The zodiac is divided into twelve signs, each associated with specific dates
of the year. They are: Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra,
Scorpio, Sagittarius, Capricorn, Aquarius, and Pisces.\n
It is believed that each sign has its own set of characteristics,
strengths, weaknesses, and compatibility with other signs. Remember that
astrology is a belief system and is not based on empirical scientific evidence.
"""
    )


def clear():
    """
    This function uses the command
    to clears the terminal screen.
    """
    print('\033c')


def print_sign(zodiac_sign):
    """
    Prints the user's zodiac sign.
    Args:
        zodiac_sign (str): The user's zodiac sign.
    """
    print(f'{"Your zodiac sign is " + zodiac_sign.upper():^60}')
    print("")


def print_instructions():
    print(" Instructions:")
    print("Choose the option that best aligns with your personality.")
    print("If your choice matches the personality description of your zodiac")
    print("sign, the compatibility progress bar will increase.")
    print("Choose from options 1 to 4. Type your choice and press 'Enter'.\n")


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
    Randomly selects a dictionary of answers.
    Args:
        answers (dict): A dictionary of zodiac signs and
        their corresponding answers.
    Returns str: A randomly selected answer list.
    """
    signs = list(answers.keys())
    return signs[random.randint(1, len(signs) - 1)]


def build_options(answers, sign):
    """
    Builds a list of answer options for a question.
    Args:
        answers (dict): A dictionary of zodiac signs and
        their corresponding answers.
        sign (str): The zodiac sign for which options are being built.
    Returns a list of shuffled options, including the correct answer.
    """
    show = [{sign: answers.pop(sign)}]
    for _ in range(1, 4):
        index = shuffle_answers(answers)
        chosen_option = answers.pop(index)
        show.append({index: chosen_option})

    return show


def test_screen(sign):
    """
    Conducts the Zodiac Traits Test for a specific zodiac sign.
    This function initiates the test, presents questions and
    options to the user, evaluates the user's responses, and
    calculates an affinity score based on correct answers. It also displays
    a progress bar to track the affinity test progress.
    Args:
        sign (str): The user zodiac sign for which the test is conducted.
    """
    clear()
    print_sign(sign)
    print_instructions()
    affinity_score = 0
    data_shuffled = shuffle_data(data)

    with tqdm(
        total=len(data_shuffled),
        ncols=60,
        bar_format="Compatibility:|{bar}|{percentage:3.0f}%",
    ) as pbar:
        for num, record in enumerate(data_shuffled):
            question = record["question"]
            all_options = record["answer"]
            options = build_options(all_options.copy(), sign)
            shuffled_options = shuffle_data(options)

            # To assemble the question
            print(f"\n\nQuestion {num + 1}/10:\n{question}\n")
            for n, option in enumerate(shuffled_options, 1):
                answer = list(option.values())[0]
                print(f"{n}: {answer}")

            # The user's input/response
            while True:
                try:
                    answer = int(input("\nEnter an answer: "))
                    if answer not in range(1, 5):
                        raise ValueError
                    answer = options[answer - 1]
                except IndexError:
                    print("Invalid option. Choose between 1 and 4")
                    continue
                except ValueError:
                    print("Invalid option. Choose between 1 and 4")
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


def result_screen(sign):
    """
    Displays the zodiac sign description and result.
    Args:
        sign (str): The zodiac sign of the user.
    """

    print(
        """
      Test complete!  This is your final result! \n
Remember, a person's personality is influenced by a variety of factors
beyond their sun sign. This test was created for fun and entertainment.
Enjoy it in a relaxed manner!"""
    )

    print(f"""
 A brief description about your zodiac sign:{sign_description[sign]}""")


def statistics(sign=None, result=None):
    """
    This function displays the previous compatibility statistics on the screen.

    Args:
        sign (str): The zodiac sign.
        result: The calculated compatibility percentage.
    """

    try:
        if result and sign:
            return update_worksheet(sign, result)
        else:
            return get_worksheet()

    except Exception as e:
        print("Unable to connect to the internet: ", e)


def draw_progressbar(worksheet):
    """
    Draws a progress bar for visualizing data from the given worksheet.
    This function takes a worksheet as input and visualizes progress data
    using a progress bar. Each zodiac sign is aligned uniformly within the
    progress bar by adding spaces at the end.
    Args:
        worksheet (list): A list of rows containing data to be visualized.
    """

    format = "|{bar}|{percentage:3.0f}%"
    word_len_max = 12

    for num, row in enumerate(worksheet):
        if num == 0:
            continue

        sign = row[0]
        responses = int(row[1])  # Number of responses
        accuracy = float(row[3])  # Accuracy percentage

        # Added a space at the end of each sign to align them in the same space
        # Example:
        # sagittarius 11 characters + 1 white space = 12
        # aries 5 characters + 7 white space = 12
        space = " " * (word_len_max - len(sign))
        display_t = f"{sign}({responses}):{space}"

        with tqdm(total=100, ncols=60, bar_format=display_t + format) as pbar:
            pbar.update(int(accuracy))
    print("")


def choose_screen(menu_id):
    """
    Takes a menu choice and executes the corresponding action.
    Args:
        menu_id (int): The ID of the chosen menu option.
    Returns: int: The menu option chosen.
    """
    result = 0
    sign = ""
    worksheet = None
    match menu_id:
        case 1:
            about_screen()

        case 2:
            clear()
            while True:
                try:
                    month = int(input("Enter the month of your "
                                      "birth (1-12): "))
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
            worksheet = statistics(sign, result)
            result_screen(sign)

        case 3:
            clear()
            print(" Affinity percentages between the characteristics of each")
            print(" sign and the answers collected in the previous tests.")
            print("*Key: Sign (Number of participants): Compatibility (%)")
            if not worksheet:
                worksheet = statistics()

            if worksheet:
                draw_progressbar(worksheet)

        case 4:
            clear()
            header()
            print("\nThank you for exploring CosmoCompatibility!")
            print("Have a great day and see you next time!\n")

    return menu_id


def main():
    """
    Handles the main flow of the program, displaying the initial
    screen and processing menu choices.
    Exits the loop if the user chooses to quit.
    """
    initial_screen()

    while True:
        result = menu()
        if result == 4:
            break


main()
