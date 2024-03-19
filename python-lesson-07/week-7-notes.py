# week 7 notes. Functions & Modules

# Functions: a block of code containing statements to be executed, can be called from other places in the code
def function_example():
    print("this is a function")

function_example() #calls the function

# input parameters 
def greet(name):
    print(f"hi {name}")

#call the function with a param
greet("Rach")

#return to end the function and output the value of the return statement
def get_average(numbers):
    total = 0
    for number in numbers:
        total = total + number

    mean = total / len(numbers)
    return mean

ratings = [5,5,4]
avg_ratings = get_average(ratings)
print(avg_ratings)

# Modules - pre-written code we can import, containing functions 
import random

i = random.randint(0,3) #module.function(params) - random number generator between 0 and 3
letters = ['A','B','C','D']
print(letters[i])
print(random.choice(letters))

def roll_dice():
    dice_0 = random.randint(1,6)
    dice_1 = random.randint(1,6)
    dice_sum = dice_0 + dice_1
    return dice_sum

print(roll_dice())

# Local modules
import greetings
greetings.greet()