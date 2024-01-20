# Tkinter in Python

- It is Python's standard GUI (Graphical User Interface) package
- It allows us to create functional desktop applications with minimal lines of code
- It is cross-platform, meaning it works on Windows, Mac, and Linux
- Comes with Python, so no need to install it

## Tkinter Fundamentals
The main components of a Tkinter application are:

- **Window** - The main window of the application
- **Widgets** - The elements that make up the application's GUI
- **Layout** - How the widgets are arranged in the window

## Tkinter Example

```python
import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")

button = tk.Button(text="Click Me", command=button_clicked)

button.pack()

window.mainloop()
```

### Explanation:

- `import tkinter as tk` - imports the tkinter package and gives it the alias `tk`

- `window = tk.Tk()` - creates a new window and assigns it to the variable `window`

- `window.title("My First GUI Program")` - sets the title of the window

- `window.minsize(width=500, height=300)` - sets the minimum size of the window

- `my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))` - creates a label widget and assigns it to the variable `my_label`

- `my_label.pack(side="left")` - packs the label widget into the window and places it on the left side

- `button = tk.Button(text="Click Me", command=button_clicked)` - creates a button widget and assigns it to the variable `button`

- `button.pack()` - packs the button widget into the window

- `window.mainloop()` - runs the application's main loop, which is an infinite loop that waits for events to happen


## Placing Widgets

There are three different ways to place widgets in a window:

- **Pack** - organizes widgets in blocks before placing them in the parent widget
- **Place** - organizes widgets by placing them in a specific position in the parent widget

- **Grid** - organizes widgets in a table-like structure in the parent widget

