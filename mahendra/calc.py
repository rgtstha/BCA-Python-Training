import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)

    if math_operation == "addition":
        entry.insert(0, f_num + float(second_number))
    elif math_operation == "subtraction":
        entry.insert(0, f_num - float(second_number))
    elif math_operation == "multiplication":
        entry.insert(0, f_num * float(second_number))
    elif math_operation == "division":
        entry.insert(0, f_num / float(second_number)) 

# Create the main window
root = tk.Tk()
root.title("CALCULATOR")

# Entry widget to display the input and result
entry = tk.Entry(root, width=16, font=('Arial', 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons on the grid
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 16),
                       command=lambda t=text: button_click(t) if t.isnumeric() or t == '.' else button_clear() if t == 'C' else button_equal() if t == '=' else button_add() if t == '+' else button_subtract() if t == '-' else button_multiply() if t == '*' else button_divide())
    button.grid(row=row, column=column)

# Run the main loop
root.mainloop()
