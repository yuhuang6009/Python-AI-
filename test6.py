#面向对象：类
# 定义类：
# class 类名: 类目首字母大写，不用_隔开命名
#     pass
# #创建对象
# 对象名.属性名1=属性值1
# 对象名.属性名2=属性值2

# 定义类-不推荐
# class Car:  
#     pass

# # 创建对象
# c1 = Car()
# # 动态的为对象添加属性
# c1.color = "red"
# c1.brand = "BMW"
# c1.name = "X5"
# c1.price = 500000

# print(c1)
# print(c1.__dict__)#将对象的所有属性以字典的形式输出
# print(c1.brand)

# 定义类-推荐
# class Car:
#     # __init__ 方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性；
#     # self：是第一个参数，表示当前所创建出来的实例对象
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的对象初始化完毕，对象属性已经添加完毕 .")

# # 创建对象
# c1 = Car(c_color="红色", c_brand="BMW", c_name="X7", c_price=800000)
# print(c1.__dict__)

# c2=Car(c_color="白色",c_brand="奔驰",c_name="E300",c_price=450000)
# print(c2.__dict__)

#实例方法
# class Car:
      #类属性
#     wheel=4
    # tax_tate=0.1
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         #实例属性
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的对象初始化完毕，对象属性已经添加完毕 .")

#     #定义实例方法 在类里面定义def叫方法
#     def running(self):#方法
#         print(f"{self.brand} {self.name} 正在高速行驶中...")

#     def total_cost(self,discount,rate):#方法
#         """""
#         param rate:税率
#         param discount:折扣
#         return:提车总费用
#         """
#         total_cost=self.price*discount+rate*self.price
#         return total_cost
# c1 = Car(c_color="红色", c_brand="BMW", c_name="X7", c_price=800000)

# #调用对象中的方法
# c1.running()
# total=c1.total_cost(0.9,0.1)
# print("提车总费用:",total)
# print(c1.wheel) #类属性使用
# 若实例属性中有"self.wheel=2" 则先使用实例属性


#魔法方法
class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕，对象属性已经添加完毕 .")

    #定义实例方法 在类里面定义def叫方法
    def running(self):#方法
        print(f"{self.brand} {self.name} 正在高速行驶中...")

    #魔法方法
    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"
    def __eq__(self,other):
        return self.price==other.price and self.brand==other.brand and self.name==other.name
    def __lt__(self, other):
        return self.price<other.price

c1 = Car(c_color="红色", c_brand="BMW", c_name="X7", c_price=800000)
print(c1)  #__str__:输出变成字符串的类型

c2 = Car(c_color="红色", c_brand="BMW", c_name="X7", c_price=800000)
print(c1==c2) #__eq__ 判断是否相等，相等返回True

c3=Car(c_color="白色",c_brand="奔驰",c_name="E300",c_price=450000)
print(c1<c3) #__lt__ 比较大小

