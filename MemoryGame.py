import random
import time
from Utils import clear_screen


def generate_sequence(difficulty):
    numbers = list()
    for i in range(difficulty):
        numbers.append(random.randint(1, 101))
    print(numbers)
    time.sleep(0.7)
    clear_screen()
    return numbers


def get_list_from_user(difficulty):
    user_list = list()
    print('After seeing the numbers enter the numbers you saw, each one separated with Enter.')
    for i in range(difficulty):
        user_list.append(int(input(f'Number {i+1} out of {difficulty}: ')))
    return user_list


def is_list_equal(list_a, list_b):
    return list_a == list_b


def play(difficulty):
    list_a = generate_sequence(difficulty)
    list_b = get_list_from_user(difficulty)
    return is_list_equal(list_a, list_b)

