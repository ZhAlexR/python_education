"""" The game_core module contains main logic of Hangman game"""
import random


def get_initial_word(path_to_file):

    """ This function takes path to file with words and return random word from the file  """

    with open(path_to_file, 'r', encoding="UTF-8") as file:
        word_list = [word.strip() for word in file]
        single_word = random.choice(word_list)
    return single_word


def write_used_words(used_word, path_to_file):

    """ This function takes word that was used in current game session and write it to file """

    with open(path_to_file, "a") as file:
        file.write(f"{used_word}\n")
    return None


def replace_letter(string, character, replace):

    """ This function replacing letter in the secret word """

    indexes = [i for i, c in enumerate(string) if c == character]
    temp = list(replace)
    for index in indexes:
        temp[index] = character
    show_string = "".join(temp)
    return show_string


def show_used_words(path_to_file):

    """ This function takes path to file with words and return random word from the file  """

    with open(path_to_file, 'r', encoding="UTF-8") as file:
        previously_used_words = file.read()
    return previously_used_words


