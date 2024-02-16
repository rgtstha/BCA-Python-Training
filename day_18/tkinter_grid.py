import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Grid Demo")
window.geometry("300x400")


input_var = tk.StringVar(master=window, value="Label")

entry_1 = ttk.Entry(window, textvariable=input_var )
entry_1.pack()

label_1 = ttk.Label(window, text="Label 1", textvariable=input_var)
label_1.pack()


window.mainloop()