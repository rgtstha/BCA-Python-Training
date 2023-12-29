# class Shape:
#     def draw(self):
#        ...


class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def draw(self):
        print(f"Drawing Rectangle of {self.height} and {self.width}")


class Square():
    def __init__(self, length):
        self.length = length
        
     
    def draw(self):
        print(f"Drawing square of length {self.length}")