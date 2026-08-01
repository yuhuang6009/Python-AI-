#元组tuple ：不可修改元素
t1=(4,3,7,18,3,9,2,2) #下标从0开始
print(type(t1))
print(t1)

print(t1[:5:1])

#统计元素个数
print(t1.count(2))
print(t1.count(1))  

#获取下标
print(t1.index(3)) #获取第一个

#解包
a,b,c,d,e,f,g,h=t1
print(a,b,c,d,e,f,g,h)
first,second,*other,last=t1
print(*other)


#利用元组交换变量
m=10
n=20
# t=m,n 组包
# n,m=t 解包
m,n=n,m 
print(m,n)
t=m,n
n,m=t

#保留小数：
avg=1.5756776
print(f"{avg:.1f}")#保留一位小数，会四舍五入

#set 集合 元素不可重复，无序即不支持索引访问，
#空集合不能用{}，{}表示的是空字典
s=set()#空集合
s1={28,9,7,8,8,3,6,10,80}
print(s1)
print(type(s1))

#pop 随机删除元素,并通过变量返回
e=s1.pop()
print(e);print(s1)

#例子
# 原始集合
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1. 找出同时选修了法语和艺术的学生
fa_set = french_set & art_set
print(f"同时选修了法语和艺术的学生: {fa_set}")

# 2. 找出同时选修了所有四门课程的学生
all_set = football_set & basketball_set & french_set & art_set
print(f"同时选修了所有四门课程的学生: {all_set}")

# 3. 找出选修了足球，但是没有选修篮球的学生
#写法1：fb_set3 = {s for s in football_set if s not in basketball_set}
# 写法2：集合差集运算符（推荐，更简洁）
fb_set3 = football_set - basketball_set
print(f"选修了足球，但是没有选修篮球的学生: {fb_set3}")

# 4. 统计每一个学生选修的课程数量
# 把所有课程集合合并成一个大列表（允许重复）
all_list = [*football_set, *basketball_set, *french_set, *art_set]
# 用集合去重，得到所有不重复的学生姓名
unique_students = set(all_list)

for s in unique_students:
    count = all_list.count(s)
    print(f"{s} 选修了 {count} 课程")


#字典 dict：键值对(key:value)来存储数据，键不能重复，可修改
#基本格式：字典名={键1:值1,键2:值2}
#键值对形式保存，键与值之间用:隔开,每个键值对之间用,隔开
dic={"name":"huangyu","age":18}
print(type(dic))
#字典中键是唯一的，但值可以重复
dic2={"name":"huangyu","name":"yuhuang"}#值名会被后面的值覆盖
print(dic2)
dic3={"name":"huangyu","name2":"yuhuang"}
print(dic3);print()

#5.字典的常见操作
#5.1 查看元素
#方式1：变量名[键名],不可以根据下标，字典里没有下标，查找元素需要根据键名
dic4={"name":"huangyu","age":18}
print(dic4["age"]);print()# 18
#print(dic4["sex"])#键名不存在时报错
#方式2：变量名.get(键名)
print(dic4.get("age"))
print(dic4.get("tel"))#键名不存在时默认返回None
print(dic4.get("tel","不存在"))#可设置返回值
print()

#5.2 修改元素
#变量名[键名]=值
dic4={"name":"huangyu","age":18}
dic4["age"]=20#通过键名修改
print(dic4);print()

#5.3 添加元素
#变量名[新键名]=值
#注意：键名存在就修改，不存在就新增
dic4={"name":"huangyu","age":18}
dic4["tel"]=123456
print(dic4);print()

#5.4 删除元素
# del
# 删除整个字典 del 字典名
dic4={"name":"huangyu","age":18}
del dic4
#print (dic) # 报错，已经被删除了，找不到这个字典
#删除指定键值对，键名不存在就会报错  del 字典名 [键名]
dic4={"name":"huangyu","age":18}
del dic4['age']
print(dic4);print()
#del dic4['tel']#没有指定的键也会报错

#clear():情况整个字典的东西，但保留这个字典
dic4={"name":"huangyu","age":18}
dic4.clear()
print(dic4)#清完后可以进行新增
dic4["age"]=18
print(dic4);print()

# pop() 删除指定键值对，键不存在就会报错
dic4={"name":"huangyu","age":18,"tel":123456}
dic4.pop("age")
print(dic4)
# dic4.pop('tell')  # 报错，不存在键名
# dic4.pop()       # 报错，没有指定键名
dic4.popitem()     # 默认删除最后一个
print(dic4)

#5.5 len()求长度
dic4={"name":"huangyu","age":18,"tel":123456}
print(len(dic4))#返回键值对数
li=[1,2,3,4]
print(len(li))
st="hello"
print(len(st));print()
#len()通用求长度

#5.6 key():返回字典里面包含的所有键名
dic4={"name":"huangyu","age":18,"tel":123456}
print(dic4.keys())
for i in dic4.keys(): #只打印出键名
    print(i)
print()

#5.7 values():返回字典里面包含的所有值
dic4={"name":"huangyu","age":18,"tel":123456}
print(dic4.values())
for i in dic4.values(): #只打印出值
    print(i)
print()    

#5.8 items():返回字典里面包含的所有键值对，键值对以元组的形式
dic4={"name":"huangyu","age":18,"tel":123456}
print(dic4.items())
for i in dic4.items():
    print(f"{i[0]}:{i[1]}")
    #print(i,type(i)) #i是元组类型，即（），所以可以用索引

#字典的运用场景
#使用键值对，存储描述一个物体的相关信息
   