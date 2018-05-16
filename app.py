# Imports the random library.
import random

# Gets the input from the user and returns it.
def get_user_input():
    user_guess = int(input('Guess the number between 0-10: '))
    return user_guess

# Generates a random number between the passed min and max parameters.
def generate_random_number(min,max):
    number = random.randint(min,max)
    return number

# Checks if the input from the user, matches the randomly generated number whom both are passed as parameters.
def check_if_user_input_matches_random_number(user_input, random_number):
    if user_input == random_number:
        return True
    else:
        return False

# Prints the results of the current guess. Takes the result parameter in True = correct guess, and False = wrong guess.
def print_result(result, number):
    if result == True:
        print("You guessed '{}' and that was correct!!".format(str(number)))
    else:
        print('Whoops! That is not correct. The answer was: ' + str(number))

# A loop that continuesly asks for a number guess, and if that guess is correct, return and break the loop.
def ask_question():
    while(True):
        user_input = get_user_input()
        random_number = generate_random_number(0, 10)
        if check_if_user_input_matches_random_number(user_input, random_number):
            print_result(True, random_number)
            return
        else:
            print_result(False, random_number)

# Initializes the application
ask_question()
