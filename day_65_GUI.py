import tkinter as tk


# Function to update the input field
def update_input(value):
    current_input = entry_input.get()
    entry_input.delete(0, tk.END)
    entry_input.insert(tk.END, current_input + value)


# Function to clear the input field
def clear_input():
    entry_input.delete(0, tk.END)


# Function to evaluate the expression and display the result
def calculate():
    expression = entry_input.get()
    try:
        result = eval(expression)
        entry_input.delete(0, tk.END)
        entry_input.insert(tk.END, str(result))
    except Exception:
        entry_input.delete(0, tk.END)
        entry_input.insert(tk.END, "Error")


# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the input field
entry_input = tk.Entry(window, width=25, justify=tk.RIGHT, font=("Arial", 14))
entry_input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=10, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(window, text=button, width=5, command=lambda value=button: update_input(value)).grid(row=row,
                                                                                                       column=col,
                                                                                                       padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the clear button
tk.Button(window, text="C", width=5, command=clear_input).grid(row=row, column=col, padx=5, pady=5)

# Start the main event loop
window.mainloop()
