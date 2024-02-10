import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x410")
        self.root.resizable(0, 0)
        
        self.result_var = tk.StringVar()
        self.result_entry = ttk.Entry(root, textvariable=self.result_var, font=('Arial', 14), justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        buttons = [
            '%', 'CE', 'C', '⇐',
            '1/x', 'x^2', '√x', '÷',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '='
        ]

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

        row_val = 1
        col_val = 0
        for button in buttons:
            ttk.Button(root, text=button, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        self.root.bind('<Return>', lambda event: self.on_button_click('='))

    def on_button_click(self, button):
        current_text = self.result_var.get()

        if button == '⇐':
            self.result_var.set(current_text[:-1])  
        elif button == 'CE':
            self.result_var.set('')  
        elif button == 'C':
            self.result_var.set('') 
        elif button == '=':
            try:
                result = eval(current_text)
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set('Error')
        elif button == '+/-':
            if current_text and current_text[0] == '-':
                self.result_var.set(current_text[1:])
            else:
                self.result_var.set('-' + current_text)
        elif button == '1/x':
            try:
                result = 1 / float(current_text)
                self.result_var.set(str(result))
            except ZeroDivisionError:
                self.result_var.set('Error')
        elif button == 'x^2':
            self.result_var.set(str(float(current_text) ** 2))
        elif button == '√x':
            try:
                result = float(current_text) ** 0.5
                self.result_var.set(str(result))
            except ValueError:
                self.result_var.set('Error')
        else:
            self.result_var.set(current_text + button)

root = tk.Tk()
app = Calculator(root)
root.mainloop()

