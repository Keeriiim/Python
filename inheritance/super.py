class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def area(self):
        return self.width * self.height


class Cube(Square):
    # The __init__ method is not necessary if you are not adding any new attributes
    def __init__(self, side_length):
        super().__init__(side_length)
    def volume(self):
        face_area = self.width * self.height
        return face_area * self.height


cube = Cube(3)
print(cube.volume()) # 27
print(cube.area()) # 9

''' Not good code
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):
    def __init__(self, width, height):
        self.width = width
        self.height = height

'''