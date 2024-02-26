## WEEK 4 - LISTS ##

# Indexes in Python are 0-based
pets = ['dog','cat','bird','frog','rabbit']
print(pets[3]) # will print frog as dog = 0
print(pets[-1]) # negative indexes numbered from the last result, rabbit in this case
print('cat' in pets) # returns TRUE
print('dog' not in pets) # returns FALSE as it is in the list

# Slice will return a list of elements from the starting index, all the way up to but not including the stopping index
# list[starting index:stopping index]
pets[2:4] # returns bird & frog in a list
pets[1:] # returns everything from 1 onwards
pets[:3] # returns everything prior 3, not including 3

# A list can contain elements of more than 1 type

## LIST MANIPULATION
# replacing - doesn't need to be the same length
pets[1:3] = ['tiger','snake','cheater']

# adding elements
farm_animals = ['cow','sheep']
animals = pets + farm_animals
print(animals)
pets.extend(farm_animals) #same result as +
pets.append('emu') #added to end of list, one at a time
pets.insert(2, 'pig') #position, new element
pets.remove('cat') #removes 1 element at a time
pets.pop(1) #removes element at the index and returns item, default is last item
del pets[2] #can remove multiple elements with a slice range

#sorting
numbers = [12, 23, -3, -3.45, 0, 192]
numbers.sort() #cannot sort if contains strings & numbers
numbers.reverse() 
print(numbers)

#length 
print(len(numbers)) # returns 6, as there a 6 elements in the list

#count
print(numbers.count(23)) # returns 1 as 23 appears once in the list
