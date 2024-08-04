import tkinter as tk
from tkinter import messagebox

def calculator(num1: int, num2: int, opt: str) -> float:
    if opt == '+':
        ans = num1 + num2
    elif opt == '-':
        ans = num1 - num2
    elif opt == '*':
        ans = num1 * num2
    elif opt == '%':
        ans = num1 % num2
    elif opt == '/':
        if num2 == 0:
            return "Error: Division by zero"
        ans = num1 / num2
    else:
        return "Error: Invalid operation"
    
    return ans

def append_text(text):
    current = entry_num1.get()
    entry_num1.delete(0, tk.END)
    entry_num1.insert(tk.END, current + text)

def set_operation(op):
    global first_num
    global operation
    first_num = entry_num1.get()
    operation = op
    entry_num1.delete(0, tk.END)
    entry_num1.insert(tk.END, first_num + ' ' + operation + ' ')

def compute():
    try:

        parts = entry_num1.get().split()
        if len(parts) != 3:
            raise ValueError("Invalid format")
        
        num1 = int(parts[0])
        num2 = int(parts[2])
        op = parts[1]
        
        result = calculator(num1, num2, op)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers and operator.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear():
    entry_num1.delete(0, tk.END)
    result_label.config(text="Result: ")


root = tk.Tk()
root.title("Simple Calculator")


tk.Label(root, text="Enter the calculation:").grid(row=0, column=0, columnspan=4)

entry_num1 = tk.Entry(root, width=20)
entry_num1.grid(row=1, column=0, columnspan=4)


buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('0', 5, 1),
]

for (text, row, col) in buttons:
    tk.Button(root, text=text, command=lambda t=text: append_text(t)).grid(row=row, column=col, sticky='nsew')


operations = [
    ('+', 2, 3), ('-', 3, 3), ('*', 4, 3), ('%', 5, 3), ('/', 6, 3)
]

for (text, row, col) in operations:
    tk.Button(root, text=text, command=lambda t=text: set_operation(t)).grid(row=row, column=col, sticky='nsew')


tk.Button(root, text='=', command=compute).grid(row=5, column=2, columnspan=2, sticky='nsew')
tk.Button(root, text='C', command=clear).grid(row=5, column=0, columnspan=2, sticky='nsew')


result_label = tk.Label(root, text="Result: ")
result_label.grid(row=6, column=0, columnspan=4)


for i in range(7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


first_num = ''
operation = ''


root.mainloop()
