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
from random import *
debugging = True
def wordle():
    # The main function to play the Wordle game.
    def random_answer():
        shuffle(ENGLISH_WORDS) #puts ENGLISH_WORDS in a random order
        for word in ENGLISH_WORDS: #go through ENGLISH_WORDS until it finds a five-letter word
            if len(word) == 5:
                return word #returns the first five-letter word
    answer_str = random_answer() #makes our answer a random five-letter word
    answer_up = answer_str.upper() #makes it all capital (very important)
    debugging and print('answer is:', answer_up) #for testing purposes, tell me what the answer is
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
        # What should happen when RETURN/ENTER is pressed.
        guess_str = word_from_row(gw.get_current_row()) #gets the word from the current row
        guess_low = guess_str.lower() #the guess but lowercase, important for comparing to
        guess_up = guess_str.upper()
        row = gw.get_current_row()
        debugging and print('guess is:', guess_up)
        debugging and print('current row is:', row)
        if is_english_five(guess_low):
            color_row(row, answer_up)
            if guess_up == answer_up:
                gw.show_message('You won!!! Congartularons')
            else:
                row += 1
                if row == 6:
                    gw.show_message(answer_up)
                else:
                    gw.set_current_row(row)
        else:
            gw.show_message("Not in word list")



    gw.add_enter_listener(enter_action)

    def word_to_row(word:str, row:int):
        # Sets a row to a specific word
        col = 0 #starts in the first column
        for letter in word: #for every letter, add that letter then advance a column
            gw.set_square_letter(row, col, letter)
            col += 1

    def color_row(row:int, answer:str):
        guess_str = word_from_row(row)
        col = 0 #resets the column for the next color
        corr_index = [] #holds the index numbers of the correct letters
        partial_answer = '' #holds the answer minus the correct letters
        for letter in answer: #colors it all grey first so the missing letters stay that way
            gw.set_square_color(row,col, MISSING_COLOR)
            col += 1
        col = 0
        for i in range(len(guess_str)): #colors all the correct letters green
            if guess_str[i] == answer[i]:
                gw.set_square_color(row, col, CORRECT_COLOR)
                corr_index.append(i) #adds the letter's index to the correct letters list
            else:
                partial_answer += answer[i] #adds the current letter to the partial answer variable
            col += 1
        col = 0 #resets the column for the next color
        debugging and print('correct letter indices are:', corr_index)
        debugging and print('remaining letters are:', partial_answer)
        used_letters = '' #stores the letters that have been used already, to avoid repeats
        for c in range(len(guess_str)): #colors the partially correct letters
            if c not in corr_index: #if the current letter's index is not the same as a correct letter's index
                if guess_str[c] in partial_answer: #if the current letter is one of the remaining letters we need to check
                        if guess_str[c] not in used_letters: #if the letter has not been used already
                            gw.set_square_color(row, col, PRESENT_COLOR)
                            used_letters += guess_str[c] #adds the letter to the already used letters
            col += 1
        debugging and print('partially correct letters are:', used_letters)



    def is_english_five(word:str) -> bool:
        if len(word) == 5 and is_english_word(word):
            return True
        else:
            return False









# Startup boilerplate
if __name__ == "__main__":
    wordle()
