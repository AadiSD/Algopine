import tkinter as tk
from tkinter import messagebox

# In-memory storage for users and votes
users = {'admin': {'password': 'admin', 'voted': False, 'voter_id': 'admin'}}
parties = {'PartyA': 0, 'PartyB': 0, 'PartyC': 0}

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    window.geometry(f"400x300+{x_position}+{y_position}")

def login():
    login_window = tk.Tk()
    login_window.title("Login")
    center_window(login_window)

    # Login function
    def authenticate():
        username = username_entry.get()
        password = password_entry.get()
        voter_id = voter_id_entry.get()

        user = users.get(username)
        if user and user['password'] == password and user['voter_id'] == voter_id:
            login_window.destroy()
            vote(username)
        else:
            messagebox.showerror("Error", "Invalid username, password, or voter ID. Try again.")

    # Widgets for login window
    tk.Label(login_window, text="Username:").pack(pady=5)
    username_entry = tk.Entry(login_window)
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Password:").pack(pady=5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)

    tk.Label(login_window, text="Voter ID:").pack(pady=5)
    voter_id_entry = tk.Entry(login_window)
    voter_id_entry.pack(pady=5)

    login_button = tk.Button(login_window, text="Login", command=authenticate)
    login_button.pack(pady=10)

    login_window.mainloop()

def vote(username):
    vote_window = tk.Tk()
    vote_window.title("Vote")
    center_window(vote_window)

    # Vote function
    def submit_vote():
        selected_party = party_var.get()
        if selected_party in parties:
            parties[selected_party] += 1
            users[username]['voted'] = True
            messagebox.showinfo("Success", f'Thank you for voting! You selected: {selected_party}')
            vote_window.destroy()
            confirm_submission()
        else:
            messagebox.showerror("Error", "Invalid party selection.")

    party_var = tk.StringVar()
    party_var.set(list(parties.keys())[0])  # Default selection

    # Widgets for vote window
    tk.Label(vote_window, text="Vote for Your Preferred Party:").pack(pady=10)

    for party in parties:
        tk.Radiobutton(vote_window, text=party, variable=party_var, value=party).pack()

    submit_button = tk.Button(vote_window, text="Submit Vote", command=submit_vote)
    submit_button.pack(pady=10)

    vote_window.mainloop()

def confirm_submission():
    confirm_window = tk.Tk()
    confirm_window.title("Confirmation")
    center_window(confirm_window)

    tk.Label(confirm_window, text="Thank you for submitting your vote!").pack(pady=20)

    confirm_button = tk.Button(confirm_window, text="Exit", command=confirm_window.destroy)
    confirm_button.pack(pady=10)

    confirm_window.mainloop()

if __name__ == "__main__":
    login()
    print("Voting Results:")
    for party in parties:
        print(f"{party}: {parties[party]} votes")