import tkinter as tk
from tkinter import messagebox
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(input_password, hashed_password):
    return hash_password(input_password) == hashed_password

def create_user(username, password):
    with open("users.txt", "a") as file:
        hashed_password = hash_password(password)
        file.write(f"{username}:{hashed_password}\n")

def login(username, entered_password):
    with open("users.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_hashed_password = line.strip().split(":")
            if username == stored_username and verify_password(entered_password, stored_hashed_password):
                messagebox.showinfo("Login Successful", "Login successful!")
                return

    messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

root = tk.Tk()
root.title("Instant Password Verification")

tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(root, text="Login", command=lambda: login(username_entry.get(), password_entry.get()))
login_button.pack(pady=10)

# Clear the file before adding users (for demonstration purposes)
with open("users.txt", "w"):
    pass

create_user("user1", "password1")
create_user("user2", "password2")
create_user("user3", "password3")

root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = root.winfo_width()
window_height = root.winfo_height()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"400x300+{x_position}+{y_position}")

root.mainloop()
