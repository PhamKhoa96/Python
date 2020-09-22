# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 23:05:25 2020

@author: phamk
"""


class Car:

     # thuộc tính đối tượng
     def __init__(self, tenxe, mausac, nguyenlieu):
        self.tenxe = tenxe
        self.mausac = mausac
        self.nguyenlieu = nguyenlieu

     # phương thức
     def dungxe(self, mucdich):
        return "{} đang dừng xe để {}".format(self.tenxe,mucdich)

     def chayxe(self):
        return "{} đang chạy trên đường".format(self.tenxe)

     def nomay(self): 
        return "{} đang nổ máy".format(self.tenxe)

# instantiate the Car class
toyota = Car("Toyota", "Đỏ", "Điện")
lamborghini = Car("Lamborghini", "Vàng", "Deisel")
porsche = Car("Porsche", "Xanh", "Gas")

# call our instance methods
print(toyota.dungxe("nạp điện"))
print(lamborghini.chayxe())
print(porsche.nomay())