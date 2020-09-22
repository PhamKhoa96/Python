# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 23:14:40 2020

@author: phamk
"""

#Class Polygon
from abc import ABC, abstractmethod

class Polygon(ABC):
    
    @abstractmethod
    def draw(self):
        pass
    
    def getArea(self):
        pass
    
    def getCircuit(self):
        pass

#Class Rectangle
class Rectangle(Polygon):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def draw(self):
        print('Rectangle have width and height')
        
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getArea(self):
        return self.width * self.height
    
    def getCircuit(self):
        return (self.width + self.height) * 2

#Class Square    
class Square(Polygon):
    
    def __init__(self, side):
        self.side = side
        
    def getSide(self):
        return self.side
        
    def draw(self):
        print('Square have 4 sides')
        
    def getArea(self):
        return self.side * self.side
    
    def getCircuit(self):
        return self.side * 4
    
rectangle = Rectangle(8, 4)
rectangle.draw()
print("Width:", rectangle.getWidth())
print("Height:", rectangle.getHeight())
print("Square:", rectangle.getArea())
print("Circuit:", rectangle.getCircuit())
print()

square = Square(10)
square.draw()
print("Side:", square.getSide())
print("Square:", square.getArea())
print("Circuit:", square.getCircuit())

'''
Đầu tiên, để có thể tạo một abstract class ta cần import 2 mô-đun là ABC và abstractmethod trong package abc.
Dùng cú pháp class abstractClassName(ABC): để khai báo Abstract class.
Dùng từ khóa @abstractmethod để chỉ ra những phương thức abstract.
Dùng cú pháp class normalClassName(abstractClassName): để implement 1 Abstract class.
Cần phải định nghĩa lại phương thức abstract trong những class con được implement từ Abstract class.
Một Abstract class không phải là một class cụ thể, nó không thể được khởi tạo.
'''