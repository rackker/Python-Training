## Week 5 Notes ##

# IF statements 
year = 2020
year_of_birth = input('Year of birth')
age = year - int(year_of_birth)

if age > 18:
    print('You\'re old')
elif age > 12 and age < 18:
    print('Shouldn\'t you be at school?')
else: 
    print('Grow up!')

# WHILE loops
i = 0
while (i < 3):
    print(i)
    i = i + 1
    # prints i for each loop, each time i < 3, so will print 0, 1 and 2

# FOR loops
numbers = [7,15,12]
for number in numbers:
    print(number)
    print(number * 2)

# BREAK statement in loops
for attempt in range(5):
    if attempt%3 == 2:
        break #terminate loop
    print('Attempt'+str(attempt))

for attempt in range(5):
    if attempt%2 == 0:
        continue #continue loop
    print('Attempt'+str(attempt))
