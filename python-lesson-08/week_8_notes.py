## Week 8 notes - object orientated programming ##

# objects have traits & behaviours (attributes) - which are methods and data attributes
# class is 'blueprint' for creating objects
# class name syntaxis is CamelCase:
# __init__ method construsts the data attributes

class RiceCooker:
    brand = 'Yum Rice' #static attribute - applies to all objects in the class RiceCooker

    def __init__(self, model_number, price):
        self.model_number = model_number
        self.price = price 

    def cook_rice(self):
        print("Rice is cooked")

    def keep_warm(self):
        print("Rice is warm")

    def greet(self, name):
        print(f"Hi {name}, this is the rice cooker model number {self.model_number}.")

#instantiat the class - create an object from it
rice_cooker_0 = RiceCooker(23483, 398.5)
print(rice_cooker_0.model_number)
print(rice_cooker_0.price)
rice_cooker_0.cook_rice()
rice_cooker_0.keep_warm()

rice_cooker_1 = RiceCooker(1244523, 379.8)
rice_cooker_1.greet("Rach")

print(rice_cooker_0.__dict__) # prints dictionary for rice cooker 0 object
print(RiceCooker.__dict__) # prints dictionary for RiceCooker class