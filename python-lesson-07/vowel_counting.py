## Week 7 Assignment - Counting Vowels ##

## set up a module with a function that counts vowels provided by a parameter

vowel_count = []
def count_vowels(string):
    lowercase = string.lower()
    as_list = list(lowercase)
    vowels = ['a','e','i','o','u']
    for letter in vowels:
        count = as_list.count(letter)
        vowel_count.append(count)

    return (sum(vowel_count))