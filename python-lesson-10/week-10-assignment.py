## WEEK 10 ASSIGNMENT: PALINDROM CHECKER APP ##
import tkinter as tk
from palindrome_checker_v3 import palindrome_checker 

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("rac.k's palindrome checker")
        self.geometry("800x300")
        self.configure(bg="#DAFFFB")
        self.label = tk.Label(self, text="Input something, and i'll check if it's a palindrome for you", font="Helvetic 16 bold", fg="#04364A", bg="#DAFFFB")
        self.label.pack(pady = 20)
        self.entry = tk.Entry(self, bg="#176B87", fg="#DAFFFB", width="50", justify="center", font="Helvetica 14")
        self.entry.pack()
        self.btn = tk.Button(self, text="Check", command=self.submit, cursor="sb_h_double_arrow", bg="#64CCC5", fg="#04364A", font="Helvetica 16 bold")
        self.btn.pack(pady=20)
        self.output_label = tk.Label(self, bg="#DAFFFB", font="Helvetica 12 italic")
        self.output_label.pack(pady=10)

    def submit(self):
        self.input_to_check = self.entry.get()
        self.output_label.config(text=palindrome_checker(self.input_to_check))

if __name__ == "__main__":
    root = Root()
    root.bind('<Return>', lambda event=None: root.submit())
    root.mainloop()

