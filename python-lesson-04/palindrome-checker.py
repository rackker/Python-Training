## PALINDROME CHECKER ##
# Rachael Kertes week 4 assignment #

# Ask a user to input a word, the script will check if it's a palindrome
word_to_check = input('Please type a word, and I\'ll tell you if it\'s a palindrome!')

# Strings can't be reversed, so convert the input into a list and reverse it first! 
check_word = list(word_to_check)
check_word.reverse()

# Now we turn the reversed list back into a string and compare it to the original input 
check_word = "".join(check_word)

if check_word == word_to_check:
    print(f'Good stuff! {word_to_check} is indeed a palindrome')
else:
    print(f'Nope! {word_to_check} is not a palindrome, try again?')