# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 23:31:37 2020

@author: phamk
"""


Các nguyên lý
Trong Python, khái niệm về OOP tuân theo một số nguyên lý cơ bản là tính đóng gói, tính kế thừa và tính đa hình.

Tính kế thừa (Inheritance): cho phép một lớp (class) có thể kế thừa các thuộc tính và phương thức từ các lớp khác đã được định nghĩa.

Tính đóng gói (Encapsulation): là quy tắc yêu cầu trạng thái bên trong của một đối tượng được bảo vệ và tránh truy cập được từ code bên ngoài (tức là code bên ngoài không thể trực tiếp nhìn thấy và thay đổi trạng thái của đối tượng đó).

Tính đa hình (Polymorphism): là khái niệm mà hai hoặc nhiều lớp có những phương thức giống nhau nhưng có thể thực thi theo những cách thức khác nhau.

Lớp (Class) và Đối tượng (Object)
Class và Object là hai khái niệm cơ bản trong lập trình hướng đối tượng.

Đối tượng (Object) là những thực thể tồn tại có hành vi.

Ví dụ đối tượng là một xe ô tô có tên hãng, màu sắc, loại nguyên liệu, hành vi đi, dừng, đỗ, nổ máy...

Lớp (Class) là một kiểu dữ liệu đặc biệt do người dùng định nghĩa, tập hợp nhiều thuộc tính đặc trưng cho mọi đối tượng được tạo ra từ lớp đó.

Thuộc tính là các giá trị của lớp. Sau này khi các đối tượng được tạo ra từ lớp, thì thuộc tính của lớp lúc này sẽ trở thành các đặc điểm của đối tượng đó.

Phân biệt giữa Đối tượng (Object) và Lớp (Class):

Đối tượng (Object): có trạng thái và hành vi.

Lớp (Class): có thể được định nghĩa như là một template mô tả trạng thái và hành vi mà loại đối tượng của lớp hỗ trợ. Một đối tượng là một thực thể (instance) của một lớp



Ví dụ về Class và Object:

class Car:

     # thuộc tính lớp
     loaixe = "Ô tô"

     # thuộc tính đối tượng
     def __init__(self, tenxe, mausac, nguyenlieu):
        self.tenxe = tenxe
        self.mausac = mausac
        self.nguyenlieu = nguyenlieu

# instantiate the Car class
toyota = Car("Toyota", "Đỏ", "Điện")
lamborghini = Car("Lamborghini", "Vàng", "Deisel")
porsche = Car("Porsche", "Xanh", "Gas")

# access the class attributes
print("Porsche là {}.".format(porsche.__class__.loaixe))
print("Toyota là {}.".format(toyota.__class__.loaixe))
print("Lamborghini cũng là {}.".format(lamborghini.__class__.loaixe))

# access the instance attributes
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( toyota.tenxe, toyota.mausac, toyota.nguyenlieu))
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( lamborghini.tenxe, lamborghini.mausac,lamborghini.nguyenlieu))
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( porsche.tenxe, porsche.mausac, porsche.nguyenlieu))
Kết quả trả về sẽ là:

Porsche là Ô tô.
Toyota là Ô tô.
Lamborghini cũng là Ô tô.
Xe Toyota có màu Đỏ. Điện là nguyên liệu vận hành.
Xe Lamborghini có màu Vàng. Deisel là nguyên liệu vận hành.
Xe Porsche có màu Xanh. Gas là nguyên liệu vận hành.
Chương trình trên tạo một lớp Car, sau đó xác định các thuộc tính, đặc điểm của đối tượng

Chúng ta truy cập thuộc tính class bằng cách sử dụng __class __.loaixe. Các thuộc tính lớp được chia sẻ cho tất cả các cá thể của lớp.

Tương tự, chúng ta truy cập các thuộc tính instance bằng cách sử dụng toyota.tenxe, toyota.mausac và toyota.nguyenlieu.

Tuy nhiên, các thuộc tính instance là khác nhau cho mỗi cá thể của một lớp.


 
Phương thức
Phương thức (Method) là các hàm được định nghĩa bên trong phần thân của một lớp. Chúng được sử dụng để xác định các hành vi của một đối tượng.

Ví dụ về Class và Method

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
Chạy chương trình, màn hình sẽ trả về kết quả:

Toyota đang dừng xe để nạp điện
Lamborghini đang chạy trên đường
Porsche đang nổ máy
Ở ví dụ này, có ba phương thức là dungxe(), chayxe() và nomay(). Chúng được gọi là phương thức instance bởi vì chúng được gọi trên một đối tượng instance (toyota, lamborghini, porsche).

Kế thừa (Inheritance)
Tính kế thừa cho phép một lớp (class) có thể kế thừa các thuộc tính và phương thức từ các lớp khác đã được định nghĩa. Lớp đã có gọi là lớp cha, lớp mới phát sinh gọi là lớp con. Lớp con kế thừa tất cả thành phần của lớp cha, có thể mở rộng các thành phần kế thừa và bổ sung thêm các thành phần mới.

# Lớp cha
class Car:

     # Constructor
     def __init__(self, hangxe, tenxe, mausac):
        # Lớp Car có 3 thuộc tính: tenxe, mausac, hang xe
        self.hangxe = hangxe
        self.tenxe = tenxe
        self.mausac = mausac

     # phương thức
     def chayxe(self):
        print ("{} đang chạy trên đường".format(self.tenxe))

     def dungxe(self, mucdich):
        print ("{} đang dừng xe để {}".format(self.tenxe, mucdich))

# Lớp Toyota mở rộng từ lớp Car.
class Toyota(Car):

     def __init__(self, hangxe, tenxe, mausac, nguyenlieu):
 # Gọi tới constructor của lớp cha (Car) 
        # để gán giá trị vào thuộc tính của lớp cha.
 super().__init__(hangxe, tenxe, mausac)

        self.nguyenlieu = nguyenlieu

     # Kế thừa phương thức cũ
     def chayxe(self):
        print ("{} đang chạy trên đường".format(self.tenxe))

     # Ghi đè (override) phương thức cùng tên của lớp cha.
     def dungxe(self, mucdich):
        print ("{} đang dừng xe để {}".format(self.tenxe, mucdich))
        print ("{} chạy bằng {}".format(self.tenxe, self.nguyenlieu))

 # Bổ sung thêm thành phần mới 
     def nomay(self):
        print ("{} đang nổ máy".format(self.tenxe))

toyota1 = Toyota("Toyota", "Toyota Hilux", "Đỏ", "Điện")
toyota2 = Toyota("Toyota", "Toyota Yaris", "Vàng", "Deisel")
toyota3 = Toyota("Toyota", "Toyota Vios", "Xanh", "Gas")

toyota1.dungxe("nạp điện")
toyota2.chayxe()
toyota3.nomay()
Kết quả trả về:

Toyota Hilux đang dừng xe để nạp điện
Toyota Hilux chạy bằng Điện
Toyota Yaris đang chạy trên đường
Toyota Vios đang nổ máy
Chương trình này tạo hai lớp kế thừa: lớp cha Car và lớp con Toyota.

Khai báo constructor mới để gán giá trị vào thuộc tính của lớp cha. Hàm super() đứng trước phương thức __init __ để gọi tới nội dung __init __ của Car.

Class Toyota kế thừa hàm chayxe() và dungxe() của class Car đồng thời sửa đổi một hành vi thể hiện ở phương thức dungxe(). Sau đó lớp con bổ sung thêm thành phần mới là nomay() để mở rộng kế thừa.

Đóng gói (Encapsulation)
Sử dụng OOP trong Python, chúng ta có thể hạn chế quyền truy cập vào trạng thái bên trong của đối tượng. Điều này ngăn chặn dữ liệu bị sửa đổi trực tiếp, được gọi là đóng gói. Trong Python, chúng ta biểu thị thuộc tính private này bằng cách sử dụng dấu gạch dưới làm tiền tố: “_” hoặc “__“.

class Computer:

     def __init__(self):
        # Thuộc tính private ngăn chặn sửa đổi trực tiếp
        self.__maxprice = 900

 def sell(self): 
        print("Giá bán sản phẩm: {}".format(self.__maxprice))

     def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()c.sell()

# thay đổi giá.
c.__maxprice = 1000
c.sell()

# sử dụng hàm setter để thay đổi giá.
c.setMaxPrice(1000)
c.sell()
Màn hình hiển thị kết quả:

Selling Price: 900
Selling Price: 900
Selling Price: 1000
Ở ví dụ này, bạn khởi tạo class Computer, sử dụng __init __() để lưu trữ giá bán tối đa của máy tính. Nhưng sau khi sử dụng, bạn có nhu cầu sửa đổi giá, tuy nhiên không thể thay đổi theo cách bình thường vì Python đã coi __maxprice là thuộc tính private. Vậy nên để thay đổi giá trị, ta sử dụng hàm setter setMaxPrice().