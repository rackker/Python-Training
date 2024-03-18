## WEEK 6 ASSIGNMENT - Dictionary of Me ##

my_name = 'Rach'

# setting up the dictionary of me 
about_me = {
    "age": 31,
    "occupation": "data analyst",
    "side hustle": "embroidery designer",
    "favourite animal": "cat",
    "pet1": {
        "name": "bailey",
        "animal": "cat",
        "colour": "black"
    },
    "pet2": {
        "name": "morgan",
        "animal": "cat",
        "colour": "tabby"
    },
    "favourite colour": "purple"
}

# printing all the info in the dictionary
for detail in about_me:
    if "pet" not in detail:
        print(f"{my_name}\'s {detail} is {about_me[detail]}")
    else:
        print(f"{my_name} has a {about_me[detail]['colour']} {about_me[detail]['animal']} called {about_me[detail]['name']}")

# practice manipulating the about_me dictionary (add, delete, update & clear)
about_me["city"] = "Melbourne"
about_me.pop("favourite animal")
about_me["favourite colour"] = "orange"
    
# repeating code to validate the changes made above
for detail in about_me:
    if "pet" not in detail:
        print(f"{my_name}\'s {detail} is {about_me[detail]}")
    else:
        print(f"{my_name} has a {about_me[detail]['colour']} {about_me[detail]['animal']} called {about_me[detail]['name']}")

# clear dictionary
about_me.clear()
print(about_me)
