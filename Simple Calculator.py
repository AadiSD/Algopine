import tkinter as tk

def on_click(button_text):
    current_text = entry.get()
    if button_text == 'C':
        clear_entry()
    elif button_text == '<':
        entry.delete(len(current_text) - 1, tk.END)
    else:
        new_text = current_text + button_text
        entry.delete(0, tk.END)
        entry.insert(0, new_text)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying the input and result
entry = tk.Entry(root, width=20, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','. ','=','+',
    ('C'),('<')
]

row_val = 1
col_val = 0

for button in buttons:
    if isinstance(button, tuple):
        button_text, col_span = button
        tk.Button(root, text=button_text, padx=25, pady=25, font=('Arial', 16),
                  command=lambda bt=button_text: on_click(bt) if bt != '=' else calculate()).grid(row=row_val, column=col_val, columnspan=col_span)
    else:
        tk.Button(root, text=button, padx=25, pady=25, font=('Arial', 16),
                  command=lambda bt=button: on_click(bt) if bt != '=' else calculate()).grid(row=row_val, column=col_val)

    col_val += col_span if isinstance(button, tuple) else 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Center the window on the screen
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = root.winfo_width()
window_height = root.winfo_height()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"313x480+{x_position}+{y_position}")

# Run the GUI
root.mainloop()
