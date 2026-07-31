#⎛⎝≥⏝⏝≤⎛⎝               #列表和字符串的知识及常用函数
s=[12,3,4,56,"hello",True] 
print(type(s)) #获取类型
print(s[0],s[-6]) #索引获取元素值
s[0]=False;print(s[0])
#del 删除
print(len(s))
l=len(s) #求元素个数
del s[5]
print(s)
#遍历
for i in s:
    print(i)

for j in range(len(s)):
    print(j)

#切片
print(s)
print(s[0:4:2])
print(s[0:5:2])  #访头不访尾，要想访问s[4]，结尾索引要到5 

s_int_float=[]

s.append(89)
s.insert(2,90)
print(s)

for i in range(len(s)):
    # if type(s[i])==type(1) or type(s[i])==type(1.1):
    if isinstance(s[i],(int,float)) and not isinstance(s[i],bool):   
        s_int_float.append(s[i])
       
#sort reverse        
s_int_float.sort()
print(s_int_float)
s_int_float.reverse()
print(s_int_float)

# N=5;j=1
# num_list=[]
# for i in range(N):
#     num=int(input(f"输入第{j}个数字:"));j+=1
#     num_list.append(num)
# print(num_list)

# print(max(num_list))
# print(min(num_list))
# print(sum(num_list)/len(num_list))

#去重复元素
# num=0
# num1_list_new=[]
# count_dict={}
# num1_list=[8,4,5,4,2,7,4,6,3,3,1,2]
# for num in num1_list:
#     if num not in num1_list_new:
#         num1_list_new.append(num)
#         count_dict[num]=1#对于普通的字典 count_dict = {}（空字典）：它不是“默认全是 0”，而是 “默认什么都没有”（连抽屉本身都没有）只有当你显式写了 count_dict[num] = 1 时，这个“抽屉”（键）才被制造出来。
#     else:
#         count_dict[num]+=1

# print(num1_list_new)
# for num in count_dict:
#     print(f"{num}:{count_dict[num]}")   

# # 合并列表
# num1_list_sum=num1_list+num1_list_new
# print(num1_list_sum)#加号前面列表的在合并列表的前面

num_list=[]
for i in range(1,21):#包前不包后，元素范围是1到20
    if i%2==0:
        num_list.append(i**2) #相当于i^2
print(num_list)

#简化方式
num_list2=[i**2 for i in range(1,21) if i%2==0]
print(num_list2)


s_size="      hello,python    "
print(s_size[0]) #字符串不支持通过索引修改
index=s_size.find("l")
print(index)
count=s_size.count("o")#出现次数
print("o:",count)
su=s_size.upper();print(su)
su=s_size.lower();print(su)
slist=s_size.split(",") #用 ","分割
print(slist)
ss=s_size.strip() #去除空格
print(ss)

sf="l"
if s_size.find("llo")==-1:
    print(False)
else:
    print(True)

s_huiwen="123321"
s_L=len(s_huiwen)
is_huiwen=True
print(s_L)
for i in range(s_L):   
    if s_huiwen[i]!=s_huiwen[s_L-i-1]:
        is_huiwen=False
        break
    
if is_huiwen:
    print("是回文字符串")
else:
    print("不是回文字符串")    
#切片反转（最简单）
# if s_huiwen == s_huiwen[::-1]:
#     print("是回文字符串")
# else:
#     print("不是回文字符串")
