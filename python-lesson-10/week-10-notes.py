## WEEK 10 NOTES ##

# building an app (GUI) in Python

import tkinter as tk
root = tk.Tk() #instantiate 
label = tk.Label(root, text='Hello World')
label.pack() #packs widgets into container
root.mainloop() 

#put app into a class - output is exactly the same
class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.label = tk.Label(self, text='Hello World')

        self.label.pack()

if __name__ == "__main__":
    root = Root()
    root.mainloop()

#what is __name__? if we import locally to another file, the __name__ will not be __main__
print(__name__)