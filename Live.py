from Utils import error
import MemoryGame
import GuessGame
import Score


def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.'


def load_game():
    try:
        print(
            'Please choose a game to play:\n\t1. Memory Game - a sequence of numbers will appear for 1 second and you '
            'have to guess it back\n\t2. Guess Game - guess a number and see if you chose like the computer')
        choice = input('Please choose a game to play:  ')
        assert choice in ['1', '2']
        difficulty = input('Please choose game difficulty from 1 to 5: ')
        assert difficulty in ['1', '2', '3', '4', '5']
        if int(choice) == 1:
            if MemoryGame.play(int(difficulty)):
                Score.add_score(int(difficulty))
            else:
                load_game()
        else:
            if GuessGame.play(int(difficulty)):
                Score.add_score(int(difficulty))
            else:
                load_game()

    except AssertionError:
        print(error)
