import tkinter as tk
import random

characters = ['josh', 'dan', 'james', 'rach']

def generate_label():
    string1 = random.choice(characters) #returns a random selection from character list
    string2 = random.choice(characters) #returns a random selection from character list

    string = string1 + " vs " + string2

    label = tk.Label(text=string)
    x = random.randrange(1000) #returns random no between 0 - 1000
    y = random.randrange(1000) #returns random no between 0 - 1000
    label.place(x=x, y=y)


root = tk.Tk()
root.title("Get ready for the next battle!")
#config window size
root.geometry("1200x1200")
#create a button
btn = tk.Button(root, text='Generate characters',command = generate_label)
btn.pack()
#if not mainloop, will only appear for a second.
root.mainloop()
