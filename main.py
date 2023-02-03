import random
from art import logo

print(logo)

welcome_massage = "Welcome to the Secret Magic Number game!\nI'm think of a number between 1 and 100."
print(welcome_massage)

choose_difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")

random_number = random.randint(1, 100)

high_message = "Too high.!"
low_message = "Too low.!"
guess_again_message = "Gues again!"
success_message = "You got it! The answer is:"

easy_counter = 10
hard_counter = 5

have_winner = False


def game(guess_num, start_num):
    if guess_num > start_num:
        print(high_message)
    elif guess_num < start_num:
        print(low_message)
    else:
        print(f"{success_message} {guess_num}!")


def next_choose(counter):
    print(f"You have {counter} attempts remaining to guess the number!")


def guess_again_print_message(counter, message):
    if counter >= 1:
        print(message)


if choose_difficulty == 'easy':
    while easy_counter > 0:
        next_choose(easy_counter)
        your_guessing = int(input("Make a guess: "))
        game(your_guessing, random_number)

        if your_guessing == random_number:
            have_winner = True
            break

        guess_again_print_message(easy_counter, guess_again_message)
        easy_counter -= 1
else:
    while hard_counter > 0:
        next_choose(hard_counter)
        your_guessing = int(input("Make a guess: "))
        game(your_guessing, random_number)

        if your_guessing == random_number:
            have_winner = True
            break
        guess_again_print_message(hard_counter, guess_again_message)
        hard_counter -= 1

if not have_winner:
    print(f"Sorry! You lose that game! The secret number was {random_number}")