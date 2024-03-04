## PALINDROME CHECKER NEW & IMPROVED##
# Rachael Kertes week 5 assignment #

# initialise the variable to qualify to start the while loop
ask_again = 'Yes'

#allows a user to start again without re-running the program
while ask_again == 'Yes':

    # Asks a user for input in the console
    user_input = input('To check if a word or sentence is a palindrome, input here (please don\'t use punctuation):')

    # First check if input is a word on sentence, output the same variable 'user input reversed' but steps to get there are slightly different
    if user_input.isalpha() == True:  # the user input is a word 
        user_input_word = list(user_input.lower())
        user_input_word.reverse()
        user_input_reversed = "".join(user_input_word)

    else: # the user input is a sentence
        user_input_sentence = list(user_input.replace(' ','').lower())
        user_input_sentence.reverse()
        user_input_reversed = "".join(user_input_sentence)

    # final if statement prints the messege depending on if the original user input (lower cased and removing spaces) matches the reversed input
    if user_input_reversed == user_input.replace(' ','').lower():
        print(f'Good stuff! {user_input} is indeed a palindrome')

    else:
        print(f'Nope! {user_input} is not a palindrome, try again?')

    # Yes will prompt the user to input another word or sentence, No will break the loop
    ask_again = input('Try another one? (type Yes or No):')
