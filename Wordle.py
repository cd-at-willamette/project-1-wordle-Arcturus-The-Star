########################################
# Name: Sophie Avery
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr): 0.16666666 (10 min)
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        word_to_row('blimp',0)
        gw.show_message(word_from_row(0))

    def word_to_row(word:str, row:int):
        # Sets a row to a specific word
        col = 0
        for letter in word:
            gw.set_square_letter(row, col, letter)
            col += 1

    def word_from_row(row:int) -> str:
        # Takes that word from the row
        word = ''
        col = 0
        for i in range(5):
            word += gw.get_square_letter(row, col)
            col += 1
        return word

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
