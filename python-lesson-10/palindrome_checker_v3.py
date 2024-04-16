import re

def palindrome_checker(user_input):
    """checks if a word or a sentance is a palindrome or not and prints a specific statement based on this."""
    user_input_alpha = filter(str.isalpha, user_input)
    cleaned_input = "".join(user_input_alpha).lower()
    cleaned_input_reversed = cleaned_input[::-1].lower()

    # handling empty user input
    try: 
        user_input[0]
        if cleaned_input == cleaned_input_reversed:
            output = f'Good stuff! {re.sub("[^a-zA-Z\\s]+","",user_input)} is indeed a palindrome'
        else:
            output = f'Nope! {re.sub("[^a-zA-Z\\s]+","",user_input)} is not a palindrome, try again?'

    except: 
        output = f"You didn\'t input anything..."
    
    return output
