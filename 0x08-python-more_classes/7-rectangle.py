#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""
class Rectangle:
    """width, hight"""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """intialise rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1


    @property
    def width(self):
        """getter with the private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter with the private instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        '''getter with the private instance'''
        return self.__height

    @height.setter
    def height(self, value):
        """setter with the private instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """return rectangle"""
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_stmbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        '''return a string representation of the rectangle'''
        return "Rectangle(" + str(self.eidth) + ", " + str(self.eidth) + ")"

    def __del__(self):
        '''called at deletion'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
