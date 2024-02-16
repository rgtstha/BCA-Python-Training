import tkinter as tk
from tkinter import ttk

def my_add():
    try:
        num1 = int(my_input1.get())
        num2 = int(my_input2.get())
        result_value = num1 + num2
        result.configure(text=f"Result: {result_value}")
    except ValueError:
        result.configure(text="Invalid input. Please enter numbers.")


def my_sub():
    try:
        num1 = int(my_input1.get())
        num2 = int(my_input2.get())
        result_value = num1 - num2
        result.configure(text=f"Result: {result_value}")
    except ValueError:
        result.configure(text="Invalid input. Please enter numbers.")
        
def my_mul():
    try:
        num1 = int(my_input1.get())
        num2 = int(my_input2.get())
        result_value = num1 * num2
        result.configure(text=f"Result: {result_value}")
    except ValueError:
        result.configure(text="Invalid input. Please enter numbers.")

def my_div():
    try:
        num1 = int(my_input1.get())
        num2 = int(my_input2.get())
        
        if num2 == 0 :
            result.configure(text="Invalid input. Please enter valid numbers.")
        else:
            result_value = num1 / num2
            result.configure(text=f"Result: {result_value}")
    except ValueError:
        result.configure(text="Invalid input. Please enter numbers.")
window = tk.Tk()
window.title("Calculator")
window.geometry("320x200")

# First Number Frame1
frame1 = tk.Frame(master=window)
frame1.pack(side='top', fill='x',pady=15)

# label and input for num1
label1 = tk.Label(master=frame1, text="First Number")
label1.pack(side='left')
my_input1 = tk.Entry(master=frame1)
my_input1.pack(side='left')

# Second Number Frame2
frame2 = tk.Frame(master=window)
frame2.pack(side='top', fill='x',pady=15)

# label and input for num1
label2 = tk.Label(master=frame2, text="Second Number")
label2.pack(side='left')
my_input2 = tk.Entry(master=frame2)
my_input2.pack(side='left')

# Buttons Frame 3
frame3 = tk.Frame(master=window)
frame3.pack(side='top', fill='x')

add_button = tk.Button(master=frame3, text=" + ", command=my_add,bg="blue",foreground="white",font=("Arial",12),width=5)
add_button.pack(side='left', padx=5)

sub_button = tk.Button(master=frame3, text=" - ", command=my_sub,bg="blue",foreground="white",font=("Arial",12),width=5)
sub_button.pack(side='left', padx=5)

mul_button = tk.Button(master=frame3, text=" * ", command=my_mul,bg="blue",foreground="white",font=("Arial",12),width=5)
mul_button.pack(side='left', padx=5)

div_button = tk.Button(master=frame3, text=" / ", command=my_div,bg="blue",foreground="white",font=("Arial",12),width=5)
div_button.pack(side='left', padx=5)

# Result
result = tk.Label(master=window, text="")
result.pack(side='top', fill='x')
# multiplication
# div_button = tk.Button(master=window, text=" / ", command=my_div,bg="blue",foreground="white",font=("Arial",12),width=5)
# div_button.pack(pady=3,side='left')

result = tk.Label(master=window, text="")
result.pack()

window.mainloop()
