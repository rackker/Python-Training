# DRY - Don't Repeat Yourself

## Playing with Numbers
num = 2
decimal = 2.2
string = 'howdy'
boolean = True

print(type(num))
print(type(decimal))
print(type(string))
print(type(boolean))

access = True
print(access)
access = False
print(access)

other_num = 4
print(num * other_num)
print(num + other_num)
print(num > other_num)

print(4 * 4) #multiply 4 times 4
print(4 ** 4) #exponentiation 4 to the power of 4
print(18 % 7) #modulo operator returns the remainder when one number is divided by another
print(12 // 3) # floor division operator divides two numbers and takes the floor integer

#BODMAS Rule
(3 + 4) #Brackets
3 ** 4 #Orders
3 / 4 #Division & Multiplication
3 + 4 #Adition & Subtraction

a = 9 ** 1 / 2
print(a)
#exponent first, then division

b = 9 ** (1 / 2)
print(b)
#now division comes first, as it's within a bracket

## Comparison operators - return a Boolean! 
8 == 7 #false, not equal
92 >= 65 #true, 92 is greater than 65

## Logical operators - input Bool values
True and True #true - checks both values are true
True and False #false 
True or False #true - check at least one is true
not False #true - negates the value

##Input function - always a string
user_name = input("what is your name?")
print(f"{user_name} smells funny")
