# Simple theme
BG_COLOR = "white"
BTN_COLOR = "light gray"
BTN_ACTIVE = "gray"
FG_COLOR = "black"
TITLE_FONT = ("Arial", 20, "bold")
BTN_FONT = ("Arial", 14)
RESULT_FONT = ("Arial", 13)
SCORE_FONT = ("Arial", 12)
import tkinter as tk
import random


# GUI setup

window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("630x420")
window.resizable(False, False)
window.configure(bg=BG_COLOR)

# Game logic

def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""

    # Add color and emoji for effect
    color = "black"
    if user_choice == computer_choice:
        result = "It's a Tie!"
        color = "#888888"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        color = "#228B22"
        scores["user"] += 1
    else:
        result = "Computer Wins!"
        color = "#B22222"
        scores["computer"] += 1

    # Add a little animation effect
    result_label.config(text="", fg=color)
    window.after(100, lambda: result_label.config(text=f"You chose: {user_choice}", fg=color))
    window.after(600, lambda: result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}", fg=color))
    window.after(1200, lambda: result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}", fg=color))
    score_label.config(text=f"Score → You: {scores['user']} | Computer: {scores['computer']}")

scores = {"user": 0, "computer": 0}




title = tk.Label(window, text="Rock, Paper, Scissors", font=TITLE_FONT, fg=FG_COLOR, bg=BG_COLOR)
title.pack(pady=10)




button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=20)


# Remove duplicate and incomplete button definitions

paper_button = tk.Button(button_frame, text="Paper", width=12, font=BTN_FONT, bg=BTN_COLOR, fg=FG_COLOR, activebackground=BTN_ACTIVE, activeforeground=FG_COLOR, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

rock_button = tk.Button(button_frame, text="Rock", width=12, font=BTN_FONT, bg=BTN_COLOR, fg=FG_COLOR, activebackground=BTN_ACTIVE, activeforeground=FG_COLOR, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=12, font=BTN_FONT, bg=BTN_COLOR, fg=FG_COLOR, activebackground=BTN_ACTIVE, activeforeground=FG_COLOR, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=12, font=BTN_FONT, bg=BTN_COLOR, fg=FG_COLOR, activebackground=BTN_ACTIVE, activeforeground=FG_COLOR, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)



# Add a border and background for effect


result_label = tk.Label(window, text="", font=RESULT_FONT, justify="center", bd=3, relief="ridge", bg="#f0f8ff", fg=FG_COLOR, width=38, height=4)
result_label.pack(pady=20)



score_label = tk.Label(window, text="Score → You: 0 | Computer: 0", font=SCORE_FONT, fg=FG_COLOR, bg=BG_COLOR)
score_label.pack()


exit_btn = tk.Button(window, text="Exit", command=window.quit, font=("Arial", 13, "bold"), bg="#e63946", fg="white", activebackground="#a4161a", activeforeground="white", width=10)
exit_btn.pack(pady=20)

window.mainloop()