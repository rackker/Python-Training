## WEEK 6 - COMPOSITE DATA TYPES ##

# Tuples ()
# immutable (cannot be changed)
rainbow_colours = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
print(rainbow_colours[1:3]) # slice will work
# rainbow_colours.append('pink') # will error as cannot be changed

# Sets {} - not ordered
base_fabrics = {"linen", "cotton", "wool"}
other_fabrics = {"denim","bamboo", "wool"}

# add elements
base_fabrics.add('cord')

# update elements
other_fabrics.update(["lycra", "spandex"])
print(other_fabrics)

# union set operator; unique values from both sets
all_fabrics = base_fabrics | other_fabrics
print(all_fabrics)
base_fabrics.union(other_fabrics) # will give the same result

# intersection set operator; duplicate values across sets
common_fabrics = base_fabrics & other_fabrics
print(common_fabrics)
base_fabrics.intersection(other_fabrics) # same result

# difference set operator - compare one set to the other
base_only = base_fabrics - other_fabrics
other_only = other_fabrics - base_fabrics
print(base_only)
print(other_only)
base_fabrics.difference(other_fabrics) # same results

# Dictionary - key value pairs {:}
base_collection = {
    "dress" : "linen",
    "skirt" : "cotton"
}

# lookup key to find value
base_collection['dress'] # returns 'linen'
print(base_collection.keys()) # returns all keys
print(base_collection.values()) # returns all values
print(base_collection.items()) # returns all KVPs

# manipulate dictionaries
base_collection["dress"] = 'viscose'
print(base_collection)
base_collection["pants"] = 'denim' # adds to dictionary
print(base_collection)
base_collection.pop("skirt") # removes from dictionary
print(base_collection)
base_collection.update({'hat':'terry','mini skirt':'cotton'}) # add to dictionary
print(base_collection)
base_collection.clear() # removes all 
print(base_collection)