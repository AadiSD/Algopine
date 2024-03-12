import tkinter as tk
from tkinter import messagebox

class CinemaTicketSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Cinema Ticket System")

        self.movie_name = tk.StringVar()
        self.movie_name.set("Movie Title")

        self.num_rows = 5
        self.seats_per_row = 10

        self.seating_chart = [[{'occupied': False, 'category': ''} for _ in range(self.seats_per_row)] for _ in range(self.num_rows)]

        self.selected_seats = []

        self.create_widgets()

    def create_widgets(self):
        # Screen Display
        screen_label = tk.Label(self.root, text="Screen", font=("Arial", 16, "bold"))
        screen_label.grid(row=0, column=0, rowspan=self.num_rows, pady=10, padx=10, sticky='n')

        # Movie Selection
        movie_label = tk.Label(self.root, text="Select Movie:")
        movie_label.grid(row=0, column=1, pady=5, sticky='w')

        movie_options = ["Movie 1", "Movie 2", "Movie 3"]  # Add your movie options here
        movie_dropdown = tk.OptionMenu(self.root, self.movie_name, *movie_options)
        movie_dropdown.grid(row=0, column=2, pady=5, sticky='w')

        # Seating Chart
        seating_label = tk.Label(self.root, text="Seating Chart:")
        seating_label.grid(row=1, column=1, columnspan=self.seats_per_row, pady=5, sticky='w')

        self.buttons = []

        for i in range(self.num_rows):
            for j in range(self.seats_per_row):
                category = self.get_category(i, j)
                button_text = f"{i+1}-{j+1}\n{category}"
                button = tk.Button(self.root, text=button_text, width=6, height=2,
                                   command=lambda row=i, seat=j: self.toggle_seat(row, seat))
                button.grid(row=i + 2, column=j + 1, padx=2, pady=2, sticky='w')
                self.buttons.append(button)

        # Confirmation Button
        confirm_button = tk.Button(self.root, text="Confirm Tickets", command=self.confirm_tickets)
        confirm_button.grid(row=self.num_rows + 2, column=1, columnspan=self.seats_per_row, pady=10, sticky='w')

        # Exit Button
        exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.grid(row=self.num_rows + 3, column=1, columnspan=self.seats_per_row, pady=10, sticky='w')

        # Center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width - self.root.winfo_reqwidth()) // 2
        y_coordinate = (screen_height - self.root.winfo_reqheight()) // 2
        self.root.geometry("+{}+{}".format(x_coordinate, y_coordinate))

    def toggle_seat(self, row, seat):
        if not self.seating_chart[row][seat]['occupied']:
            self.seating_chart[row][seat]['occupied'] = True
            self.selected_seats.append((row + 1, seat + 1, self.seating_chart[row][seat]['category']))
        else:
            self.seating_chart[row][seat]['occupied'] = False
            self.selected_seats.remove((row + 1, seat + 1, self.seating_chart[row][seat]['category']))

        self.update_button_colors()

    def update_button_colors(self):
        for i in range(self.num_rows):
            for j in range(self.seats_per_row):
                category = self.seating_chart[i][j]['category']
                button_text = f"{i + 1}-{j + 1}\n{category}"
                button_index = i * self.seats_per_row + j
                if self.seating_chart[i][j]['occupied']:
                    self.buttons[button_index].configure(bg="red")
                    self.buttons[button_index].configure(text=f"{button_text}\n(Selected)")
                else:
                    color = self.get_category_color(category)
                    self.buttons[button_index].configure(bg=color, text=button_text)

    def get_category_color(self, category):
        # You can customize the button colors based on the category
        if category == "Recliner":
            return "blue"
        elif category == "Stall":
            return "green"
        elif category == "Balcony":
            return "orange"
        else:
            return self.root.cget("bg")  # Use the default background color of the root window

    def confirm_tickets(self):
        if not self.selected_seats:
            messagebox.showwarning("No Tickets Selected", "Please select at least one seat before confirming.")
            return

        ticket_summary = "\n".join([f"Row {row}, Seat {seat}, Category: {category}" for row, seat, category in self.selected_seats])
        total_cost = len(self.selected_seats) * self.get_category_price(self.selected_seats[0][2])

        confirmation_message = f"Ticket Summary:\n{ticket_summary}\n\nTotal Cost: ${total_cost}"
        confirmed = messagebox.askyesno("Confirm Tickets", confirmation_message)

        if confirmed:
            # You can add further actions here, such as saving the ticket information to a file or database.
            messagebox.showinfo("Tickets Confirmed", "Thank you for your purchase!")
            # Optionally, you can reset the selected seats after confirmation
            self.reset_seats()

    def reset_seats(self):
        self.selected_seats = []
        for i in range(self.num_rows):
            for j in range(self.seats_per_row):
                self.seating_chart[i][j]['occupied'] = False

        self.update_button_colors()

    def get_category(self, row, seat):
        if row + 1 <= 5 and seat + 1 == 1:
            return "Recliner"
        elif seat + 1 == 2 or (seat + 1 == 3 and row + 1 <= 5):
            return "Stall"
        else:
            return "Balcony"

    def get_category_price(self, category):
        # You can customize the pricing based on the category
        if category == "Recliner":
            return 25  # Adjusted price for Recliner seats
        elif category == "Stall":
            return 20  # Adjusted price for Stall seats
        elif category == "Balcony":
            return 15  # Adjusted price for Balcony seats
        else:
            return 10  # Default price

if __name__ == "__main__":
    root = tk.Tk()
    app = CinemaTicketSystem(root)
    root.mainloop()
