import tkinter as tk
from tkinter import ttk
from add_book_window import AddBookWindow

class LibrarySystem(tk.Tk):
   def __init__(self):
      super().__init__()
      self.title("Library Management System")
      self.geometry("900x600")
      self.create_widgets()

   def create_widgets(self):
      add_book_button = ttk.Button(master=self, text="Add Book", command=self.show_add_book)
      add_book_button.pack(anchor="w", padx= 20, pady=20)

      book_tree = ttk.Treeview(master= self, columns=( 'name', 'author', 'isbn'), show='headings')
      book_tree.heading('name', text= 'Full Name', anchor='w')
      book_tree.heading('author', text= 'Author Name', anchor='w')
      book_tree.heading('isbn', text= 'ISBN', anchor='w')
      book_tree.pack(anchor='w', padx= 20, pady=20)

      book_tree.insert(parent='', index= tk.END, values=("ram", 'Shyam', '2332'))

   def show_add_book(self):
      AddBookWindow()


library = LibrarySystem()
library.mainloop()




# add_student_button = ttk.Button(master=root, text= "Add Student")
# add_student_button.pack(anchor="w", padx=20, pady=20)

# student_tree = ttk.Treeview(master= root, columns=('S.N', 'Name', 'Email', 'Phone', 'Address'))
# student_tree.heading('S.N', text='S.N' , anchor="w")
# student_tree.heading('Name', text='Name')
# student_tree.heading('Email', text='Email')
# student_tree.heading('Phone', text='Phone')
# student_tree.heading('Address', text='Address')
# student_tree.pack(padx= 20, pady= 20)

# root.mainloop()