########################################
# Name: Sophie Avery
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.
    gw = WordleGWindow()
    def word_from_row(row:int) -> str:
        # Takes that word from the row
        word = '' #empty string to add letters to
        col = 0 #starts at the beginning
        for i in range(5): #all the words are 5 letters long
            word += gw.get_square_letter(row, col)
            col += 1 #advance to the next column
        return word

    def enter_action():
        guess_str = word_from_row(0)
        guess_low = guess_str.lower()
        guess_cap = guess_str.upper()
        # What should happen when RETURN/ENTER is pressed.
        if is_english_five(guess_low):
            gw.show_message("That's a five letter English word")
        else:
            gw.show_message("Not in word list")

    gw.add_enter_listener(enter_action)

    def word_to_row(word:str, row:int):
        # Sets a row to a specific word
        col = 0 #starts in the first column
        for letter in word: #for every letter, add that letter then advance a column
            gw.set_square_letter(row, col, letter)
            col += 1



    def is_english_five(word:str) -> bool:
        if len(word) == 5 and word in ENGLISH_WORDS:
            return True
        else:
            return False






# Startup boilerplate
if __name__ == "__main__":
    wordle()
