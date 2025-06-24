import tkinter as tk
import random

# Game options
choices = ["Rock", "Paper", "Scissors"]

# Scores
user_score = 0
comp_score = 0

# Game logic
def play(user_choice):
    global user_score, comp_score

    comp_choice = random.choice(choices)
    result = ""

    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        comp_score += 1

    # Update the result and scores
    result_label.config(text=f"You chose {user_choice}\nComputer chose {comp_choice}\n{result}")
    score_label.config(text=f"Your Score: {user_score}  |  Computer Score: {comp_score}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.configure(bg="#f0f0f0")

# Labels
tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"), bg="#E57373").grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"), bg="#81C784").grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"), bg="#64B5F6").grid(row=0, column=2, padx=5)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="black")
result_label.pack(pady=20)

# Score display
score_label = tk.Label(root, text="Your Score: 0  |  Computer Score: 0", font=("Arial", 12), bg="#f0f0f0")
score_label.pack()

# Restart game (reset scores)
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_label.config(text="")
    score_label.config(text="Your Score: 0  |  Computer Score: 0")

tk.Button(root, text="Reset Game", command=reset_game, bg="#FFB74D", fg="black").pack(pady=10)

# Run the app
root.mainloop()
