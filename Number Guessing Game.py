import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.lower_bound = tk.IntVar(value=1)
        self.upper_bound = tk.IntVar(value=100)
        self.secret_number = random.randint(self.lower_bound.get(), self.upper_bound.get())
        self.attempts = 0
        self.max_attempts = 10
        self.level = 1

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Select your preferred range of numbers:")
        self.label.pack(pady=10)

        self.lower_bound_label = tk.Label(self.master, text="Lower Bound:")
        self.lower_bound_label.pack()
        self.lower_bound_entry = tk.Entry(self.master, textvariable=self.lower_bound)
        self.lower_bound_entry.pack(pady=5)

        self.upper_bound_label = tk.Label(self.master, text="Upper Bound:")
        self.upper_bound_label.pack()
        self.upper_bound_entry = tk.Entry(self.master, textvariable=self.upper_bound)
        self.upper_bound_entry.pack(pady=10)

        self.range_button = tk.Button(self.master, text="Set Range", command=self.set_range)
        self.range_button.pack(pady=5)

        self.guess_label = tk.Label(self.master,
                                    text="Guess the number between {} and {}".format(self.lower_bound.get(),
                                                                                     self.upper_bound.get()))
        self.guess_label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.feedback_label = tk.Label(self.master, text="")
        self.feedback_label.pack(pady=10)

    def center_window(self, width, height):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.master.geometry("{}x{}+{}+{}".format(width, height, x, y))

    def set_range(self):
        try:
            lower_bound = int(self.lower_bound.get())
            upper_bound = int(self.upper_bound.get())

            if lower_bound >= upper_bound:
                messagebox.showerror("Error", "Upper bound must be greater than lower bound.")
            else:
                self.lower_bound.set(lower_bound)
                self.upper_bound.set(upper_bound)
                self.secret_number = random.randint(lower_bound, upper_bound)
                self.guess_label.config(text="Guess the number between {} and {}".format(lower_bound, upper_bound))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for the bounds.")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess == self.secret_number:
                messagebox.showinfo("Congratulations",
                                    "You guessed the correct number {} in {} attempts.".format(self.secret_number,
                                                                                               self.attempts))
                self.level_up()
                self.master.destroy()
            elif guess < self.secret_number:
                self.give_feedback("Too low.")
            else:
                self.give_feedback("Too high.")

            if self.attempts == self.max_attempts:
                self.give_feedback(
                    "Game Over: You've reached the maximum number of attempts. The correct number was {}.".format(
                        self.secret_number))
                self.master.destroy()
        except ValueError:
            self.give_feedback("Error: Please enter a valid number.")

    def level_up(self):
        messagebox.showinfo("Level Up!", "Congratulations! You've successfully guessed the number and leveled up.")
        self.level += 1
        self.max_attempts += 2  # Increase the difficulty by reducing the number of attempts allowed

    def give_feedback(self, feedback):
        if abs(self.secret_number - int(self.entry.get())) < 10:
            if self.secret_number - int(self.entry.get()) > 0:
                feedback += " You are close! Go higher."
            else:
                feedback += " You are close! Go lower."
        self.feedback_label.config(text=feedback)


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    app.center_window(400, 350)  # Set the width and height of the window
    root.mainloop()
