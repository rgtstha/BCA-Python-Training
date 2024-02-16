import tkinter as tk
from tkinter import ttk


# def addition():
#     num1 = num_1_text_field.get()
#     num2 = num2_text_field.get()

#     total = int(num1) + int(num2)
#     result.configure(text= total)


# def subtraction():
#     num1 = num_1_text_field.get()
#     num2 = num2_text_field.get()

#     total = int(num1) - int(num2)
#     result.configure(text= total)


window = tk.Tk()
window.title("Calculator")
window.geometry("300x200")


label_1 = ttk.Label(text="First Number")
label_1.pack(side= "left")

num_1_text_field = ttk.Entry()
num_1_text_field.pack(side="left")

# num2_text_field = ttk.Entry()
# num2_text_field.pack(side="left")

# add_button = ttk.Button(text="Add", command= addition)
# add_button.pack(side="left")

# sub_button = ttk.Button(text="Subtract", command= addition)
# sub_button.pack()

# mul_button = ttk.Button(text="Multiply", command= addition)
# mul_button.pack()

# result = ttk.Label(  text= "Result", font=("Arial", 40), background="red")
# result.pack()

window.mainloop()