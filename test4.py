#函数
def circle_area_len(r):
    return 3.14*r*r,2*3.14*r

al=circle_area_len(10)
print(al,type(al)) #多个返回值返回的是元组
#解包：
area,round_len=circle_area_len(10)
# print(area,round_len)
print(f"{area},{round_len:.1f}")

#案例：第义一个函数，计算传入字符串中元音字母的个数：aeiouAEIOU
def count_aeiou(s):
    num=0
    for i in s:
        if i in "aeiouAEIOU":
            num+=1
    return num
print(count_aeiou("hello world"))

#案例：传入学生成绩列表，计算最高分，最低分，平均分(保留一位小数)并返回
def calf_score(score_list):
    max_s=max(score_list)
    min_s=min(score_list)
    ave_s=round(sum(score_list)/len(score_list),1)#round(,1)表示保留一位小数
    return max_s,min_s,ave_s

s_list=[12,32,24,56,65,43,76,59]
print("最高分,最低分,平均分")
print(calf_score(s_list))
max_score,min_score,ave_score=calf_score(s_list) #解包
print(f"最高分:{max_score},最低分:{min_score},平均分:{ave_score}")

def all_math_grade(first_score,second_score,third__score):
    return first_score,second_score,third__score

print(all_math_grade(89,78,90)) #参数意义不明确时，用对应位置传参数，代码可读性差
print(all_math_grade(first_score=89,second_score=78,third__score=90))#关键字传参数

def main_intro(c,r=2): #r=2默认参数
    return c,r
print(main_intro(1))

#可变参数
# 含义: 传入的值的数量是可以改变的，可以传入多个，也可以不传
# 格式: def func(*args)
def func(*args):
    print(args)
    print(type(args))  # 以元组形式接收
func("海绵宝宝", "派大星星", "章鱼哥哥")

#关键字参数
# 格式: def func(**kwargs)
def fund(**kwargs):
    print(kwargs)
    print(type(kwargs))  # 以字典形式接收
fund()  # 空字典
fund(name='bingbing', age=18)  # 传值的时候，需要采用键=值的形式
#作用: 可以扩展函数的功能

#案例 :不定长参数
# 需求：根据传入的这批数据，计算这批数据的最小值，最大值，平均值
def calc_data(*args, **kwargs):
    """
    根据传入的这批数据，计算这批数据的最小值，最大值，平均值
    :param args: 不定长位置参数，需要计算的这批数据
    :param kwargs: 不定长关键字参数
        round: 保留的小数位个数
        print: 是否打印输出
    :return: 最小值，最大值，平均值
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    # 判断是否传入round，进行小数保留
    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))

    # 判断是否需要内部打印结果
    if kwargs.get("print"):
        print(f"计算出来的最小值: {min_data}, 最大值: {max_data}, 平均值:{avg_data}")

    return min_data, max_data, avg_data


# 调用函数
print(calc_data(2, 7, 9, 10, 45, round=3, print=True))
print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222,round=2,print=False))

#函数作为参数
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
#计算
def calc(x,y,oper):
    return oper(x,y)
#oper:该位置用于填具体函数操作

print(calc(10,20,add))
print(calc(10,20,subtract))

#递归
def jc(n):
    if n==1:
        return 1
    else:
        return n*jc(n-1)

print(jc(10))    