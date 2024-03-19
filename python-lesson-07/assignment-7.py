## Week 7 Assignment (part 2) ##

# Call vowel checking module set up in vowel_counting.py

import vowel_counting

user_name = input("what is your name?: ")
count_of_vowels = vowel_counting.count_vowels(user_name)
print(f"your name is {user_name}, your name contains {count_of_vowels} vowels")