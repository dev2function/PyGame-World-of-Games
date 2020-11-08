import os
error = 'ERROR_MESSAGE: "Something went wrong..'
SCORES_FILE_NAME = 'scores.txt'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def BAD_RETURN_CODE():
    return None
