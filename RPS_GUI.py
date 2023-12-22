import tkinter as tk
from tkinter import messagebox
import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"


class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(root, text="Welcome to the Rock-Paper-Scissors Game!\nChoose an option below:")
        self.label.pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.create_button("Rock")
        self.create_button("Paper")
        self.create_button("Scissors")

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Score - You: 0 | Computer: 0")
        self.score_label.pack(pady=10)

    def create_button(self, choice):
        button = tk.Button(self.buttons_frame, text=choice, command=lambda: self.play(choice))
        button.pack(side=tk.LEFT, padx=5)

    def play(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        result = determine_winner(user_choice, computer_choice)
        self.display_result(user_choice, computer_choice, result)

        # Update scores
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1

        # Update score label
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")

    def display_result(self, user_choice, computer_choice, result):
        message = f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}"
        self.result_label.config(text=message)
        messagebox.showinfo("Game Result", message)


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
