from employee import Employee

class Developer(Employee):
    # developer may have some unique attributes like, programming language, 
    def __init__(self, name, id, salary, language):
        super().__init__(name, id, salary)
        self.language = language

    def display(self): # overriding
        # super().display()
        print(f" Language: {self.language}")