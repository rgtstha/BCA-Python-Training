from employee import Employee

class Designer(Employee):
    # designer may have some unique attributes like, designing tool, 
    def __init__(self, name, id, salary, tool):
        super().__init__(name, id, salary)
        self.tool = tool

    def display(self):
        super().display()
        print(f" Tool: {self.tool}")
