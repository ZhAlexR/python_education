import colorama
from python_education.hangman.game_core import get_initial_word, write_used_words, replace_letter, show_used_words


def game_process():

    """ Main game process was realised in this function"""

    given_word = (get_initial_word('initial_words.txt'))
    write_used_words(given_word, "used_words.txt")
    show_letter_number = "_" * len(given_word)
    print(show_letter_number)
    missed_letter = []
    guessed_letter = []
    tries = 6

    while tries > 0 and given_word != show_letter_number:

        user_letter = input("Enter your letter: ").lower()

        if user_letter in given_word:
            guessed_letter.append(user_letter)
            print(f"{colorama.Fore.GREEN}Correct! The letter {user_letter} in the word{colorama.Fore.RESET}")
            show_letter_number = replace_letter(given_word, user_letter, show_letter_number)
            print(show_letter_number)
            print(f"Missed letter list: {missed_letter}")

        else:
            tries -= 1
            missed_letter.append(user_letter)
            print(f"{colorama.Fore.RED}Incorrect! There is no latter '{user_letter}'{colorama.Fore.RESET}\n"
                  f"Missed letter list: {missed_letter}")
        print(f"{colorama.Fore.GREEN}You have {tries} try(-ies){colorama.Fore.RESET}")
        print("****************\n")
    result = (given_word, tries)
    return result


def show_results(result_tuple):

    """ This function shows game result to user.
        It takes result like a tuple from function game process """

    if result_tuple[1] > 0:
        print(f"Congratulations!!! You won\n "
              f"The word was {result_tuple[0]}")
    else:
        print(f"I'm sorry, but you hung the little man! Have more concentration next time!\n"
              f"The word was {result_tuple[0]}")


if __name__ == "__main__":
    option = {1: "start", 2: "show previously words", 3: "exit"}
    while True:
        user_input = int(input(f"Please choose the option {option}: "))
        if user_input == 1:
            show_results(game_process())
        elif user_input == 2:
            word_list = show_used_words("used_words.txt")
            print(word_list)
        elif user_input == 3:
            break

        else:
            print(f"{colorama.Fore.RED}Please, choose correct option {colorama.Fore.RESET} ")
