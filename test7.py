#异常处理 #
try:
    # print(my_name)
    # print(1/0)
    print("ABC"[10]) #本应该是索引错误，但没有except IndexError as e,所以由except Exception as e兜底
except NameError as e: #捕获的是NameError类型的异常
    print("程序运行出错,名称不存在,异常信息:",e)
except ZeroDivisionError as e:
    print("程序运行出错,0不能被除,异常信息:",e)

# 如except NameError as e 这种只能捕获单个异常
# 若要捕获全部异常
except Exception as e:
    print("程序运行出错异常信息:",e)
finally: #无论什么情况都会运行
    print("资源释放")

# 异常的传递
def fun1():
    print("fun1 ... running ...")
    fun2()

def fun2():
    print("fun2 ... running ...")
    fun3()

def fun3():
    print("fun3 ... running ...")
    print(my_color)

if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print("程序运行出错了，请联系管理员，错误信息：", e)




# 抛出异常 raise
# 步骤:
# 1. 创建一个Exception('xxx')对象，xxx---异常提示信息
# 2. raise抛出这个对象(异常对象)
# raise Exception("冰冰抛出了一个异常")
# def funa():
#     raise Exception("冰冰抛出了一个异常")
#     print("哈哈哈，笑死我了")
# funa()

# if __name__=='__main__':
#     try:
#         fun2()
#     except Exception as e:
#        print("程序运行出错了，请联系管理员，错误信息：", e)    
        