a,b,c=100,200,300  #9_36python基础内容
d=a;e=b;f=c
c=d;a=e;b=f;
print(a,b,c)
s="""
    亲爱的同学们，老师们：
    大家早上好！    
"""
print(s)
s2='it\'is a wonderful day'#转义字符\
s2="it'is a wonderful day"
print(s2)

#转变量类型
name ="haung"
age=18
habit="surf Internet"
msg="like"
print("我是"+name+"年龄是"+str(age)+"并且"+msg+" "+habit)
print(f"姓名：{name} ,年龄：{age} ,爱好：{habit} ")
# x=int(input("输入一个整数x:"))
# y=int(input("输入一个整数y:"))
# print("x+y=",x+y,sep="")
# x=(input("输入一个整数x:"))
# y=(input("输入一个整数y:"))
# print("字符串拼接：x+y=",x+y)
# x=float(input("输入一个浮点数x:"))#x=0.5
# y=float(input("输入一个浮点数y:"))#y=0.4
# print("x-y:",x-y) #x-y=0.9999999
# print("x+y",x+y)

f_a=0.5
f_b=0.4
print(f_a-f_b) #浮点数在计算时可能会出现偏差，原因是二进制无法准确的表示所有小数

print(100==101)#False

#if-else
# year=int(input("输入年份："))
# if (year%400==0) or (year%4==0 and year%100!=0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

# day=(input("今天是星期(1-7)"))
# match day:
#     case "1":
#         print("周一")
#     case "2":
#         print("周二")
#     case "3":
#         print("周三")
#     #相当于switch-case
#     case _:
#         print("输入错误")

#循环：
i=0
while i<10:
    i+=1
    print("我是执行语句")
else:
    print("执行完成")   #可选

name="huang"
for i in name:
    print(i)
for i in range(6):
    print(i,end=" ")    #默认：end="\n"
print()#相当于\n,省略print(end="\n")

for i in range(100,501):
    if(i%2==0):
        print(i,end=" ")
print()

#嵌套
for i in range(1,10):
    for j in range(1,i+1):
       print(f"{j} x {i} = {j*i}",end="\t")
    print()

import random
random_num=random.randint(1,100)#随机生成1到100的随机数
while True:
    num=int(input("输入一个数字"))
    if num > random_num:
        print("数字大了，小一点")
    elif num < random_num:
        print("数字小了，大一点")
    else:
        print("猜对了")
        break    

