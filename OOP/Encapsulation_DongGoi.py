# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 23:08:50 2020

@author: phamk
"""


class Computer:

     def __init__(self):
        # Thuộc tính private ngăn chặn sửa đổi trực tiếp
        self.__maxprice = 900

     def sell(self): 
        print("Giá bán sản phẩm: {}".format(self.__maxprice))

     def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# thay đổi giá.
c.__maxprice = 1000
c.sell()

# sử dụng hàm setter để thay đổi giá.
c.setMaxPrice(1000)
c.sell()