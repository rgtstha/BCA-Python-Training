import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", ".", "/",
    "="
]


def button_handler(key):
    if key == "=":
        value = eval(entry_value.get())
        entry_value.set(value)
    
    elif key == 'C':
        entry_value.set('0')
    else:   
        entry_value.set(entry_value.get() + key)

window.rowconfigure((0,1,2,3,4,5), weight=1)
window.columnconfigure((0,1,2,3,4), weight=1)


entry_value = tk.StringVar()

entry_box = ttk.Entry(justify="right", textvariable=entry_value, font=("Arial", 20))
entry_box.grid(row=0, column=0, sticky="ewns", columnspan=4)

row_count = 1
col_count = 0

for i in range(len(buttons)):
    if buttons[i] == '=':
        button = ttk.Button(text = buttons[i], command= lambda x = buttons[i]: button_handler(x))
        button.grid(row=row_count, column=col_count, columnspan=4, sticky="ewns")
    else:
        button = ttk.Button(text=buttons[i], command= lambda x = buttons[i]: button_handler(x))
        button.grid(row=row_count, column=col_count, sticky="ewns")

    col_count = col_count + 1
    if(col_count> 3):
        row_count = row_count + 1
        col_count = 0

window.mainloop()