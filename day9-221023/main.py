class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

# def add(a, b):
#     if type(a) =='str':
#         return 0
#     return a + b
# print(type('5').__name__)

def test_normal_case():
    rectangle = Rectangle(2, 3)
    assert rectangle.get_area() == 6, 'incorrect area'

a = 10
a = '10'