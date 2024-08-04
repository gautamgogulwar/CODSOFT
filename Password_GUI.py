import random
import tkinter as tk
from tkinter import messagebox


le = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sy = ['!', '@', '#', '$', '%', '(', ')', '?']
nu = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def generate_password():
    try:
        let = int(letter_entry.get())
        sym = int(symbol_entry.get())
        num = int(number_entry.get())

        password = []
        for i in range(let):
            password.append(random.choice(le))
        for i in range(sym):
            password.append(random.choice(sy))
        for i in range(num):
            password.append(random.choice(nu))

        random.shuffle(password)
        password_str = ''.join(password)
        
        result_label.config(text=f"Generated password: {password_str}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers for letters, symbols, and numbers")


root = tk.Tk()
root.title("Password Generator")


tk.Label(root, text="Number of Letters:").grid(row=0, column=0)
letter_entry = tk.Entry(root)
letter_entry.grid(row=0, column=1)

tk.Label(root, text="Number of Symbols:").grid(row=1, column=0)
symbol_entry = tk.Entry(root)
symbol_entry.grid(row=1, column=1)

tk.Label(root, text="Number of Numbers:").grid(row=2, column=0)
number_entry = tk.Entry(root)
number_entry.grid(row=2, column=1)


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, columnspan=2)


result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)


root.mainloop()
