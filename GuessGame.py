import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    return input(f'Please pick a number between 1 {difficulty} ')


def compare_results(difficulty, secret_number):
    return int(difficulty) == int(secret_number)


def play(difficulty):
    num1 = generate_number(difficulty)
    num2 = get_guess_from_user(difficulty)
    return compare_results(num1, num2)
