## WEEK 8 ASSIGNMENT - Smart Device updates ##

# Add a default argument for install_app method.
# Modify install_app method to avoid duplicates in app_list.
# Add a delete_app method which takes in one parameter: the name of the app you would like to delete.
# Create a SmartDevice object and use it to call the functions. 
# Use print statements to check if both methods work as you expect them to.


class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name="Demo"):
    # updated to check if app is already in the app_name list
        if app_name in self.app_list:
            print(f"{app_name} already installed")
        else:
            print(f"Installing {app_name}...")
            self.app_list.append(app_name)
        return self.app_list
    
    #adding a delete_app method
    def delete_app(self, app_name):
        if app_name in self.app_list:
            self.app_list.pop()
            print(f"{app_name} uninstalled")
        else:
            print(f"cannot uninstall {app_name}, not installed...")
        return self.app_list


device_a = SmartDevice(1233244, 'CLG', 5.7)
device_a.report()

device_b = SmartDevice(112233, 'rac.k', 6)
print(device_b.app_list) # check that app list is empty by default
device_b.install_app() # default of Demo should install as no arguement passed in brackets 
device_b.install_app() # repeating it should return 'already installed' as Demo is already in the app_list
device_b.install_app("python") # installing new app called python
device_b.delete_app("python") # uninstalling app called python
device_b.delete_app("excel") # trying to uninstall a different app that has not been installed
print(device_b.app_list) # print to see what the final app_name list looks like