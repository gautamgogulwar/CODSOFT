import tkinter as tk
import random

def play_game(user_choice):
    obj = ["Stone", "Paper", "Scissor"]
    comp_choice = random.randint(0, 2)

    user_choice_text.set(f"User: {obj[user_choice]}")
    comp_choice_text.set(f"Comp: {obj[comp_choice]}")

    if user_choice == comp_choice:
        result_text.set("It's A TIE!!")
    elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
        result_text.set("USER WINS!!!!")
    else:
        result_text.set("USER LOSES")

# Create the main window
root = tk.Tk()
root.title("Stone Paper Scissors") 

# Define StringVars to update text in the GUI
user_choice_text = tk.StringVar()
comp_choice_text = tk.StringVar()
result_text = tk.StringVar()

# Create labels to display the choices and result
user_label = tk.Label(root, textvariable=user_choice_text, font=("Helvetica", 16))
comp_label = tk.Label(root, textvariable=comp_choice_text, font=("Helvetica", 16))
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 16))

# Pack the labels into the window
user_label.pack()
comp_label.pack()
result_label.pack()

# Create buttons for the user to make a choice
tk.Button(root, text="Stone", command=lambda: play_game(0), font=("Helvetica", 16)).pack(side=tk.LEFT, padx=10, pady=10)
tk.Button(root, text="Paper", command=lambda: play_game(1), font=("Helvetica", 16)).pack(side=tk.LEFT, padx=10, pady=10)
tk.Button(root, text="Scissor", command=lambda: play_game(2), font=("Helvetica", 16)).pack(side=tk.LEFT, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
