import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Library Management System")
window.geometry("500x500")

# Label
label = ttk.Label(master=window, text = "My Label")
label.pack()


#Input field
my_input = ttk.Entry(master=window)
my_input.pack()

def my_add():
    label.configure(text = my_input.get())

#Button
add_button = ttk.Button(master= window, text = "Add", command= my_add)
add_button.pack()


window.mainloop()