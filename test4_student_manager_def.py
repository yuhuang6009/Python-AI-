#练习：学生成绩管理系统
# 一个学生 = 一个字典
#student = {"id": "2024001", "name": "小明", "score": 85}
students = []
# student={}
def add_student(students):      # 添加学生
    student = {}
    student["id"]=input("学号：")
    for stu in students:
        if student["id"]==stu["id"]:
            print("学号已存在")
            break
    else:
        student["name"]=input("姓名：")
        student["score"]=int(input("成绩："))
        students.append(student)
        
def show_all(students):         # 查看所有
    for i in students:
        print(i)

def find_student(students):     # 按学号查找
    id_student=input("输入学生学号:")
    for stu in students:
        if id_student==stu["id"]:
            print(stu)
            break
    else:
        print("查找不到该学生") 
def show_stats(students):       # 统计
    if len(students)==0:
        print("还没有学生，请先添加")
    else:
        sum=0;ave=0;max_score=0;min_score=0;count=0
        max_score = students[0]["score"]  # 先拿第一个当基准
        min_score = students[0]["score"]
        for stu in students:
            sum+=stu["score"]
            ave=sum/len(students)
            if stu["score"] > max_score:
                max_score = stu["score"]
            if stu["score"] < min_score:
                min_score = stu["score"]
            if stu["score"]<60:
                count+=1
        print(f"平均分:{ave},最高分:{max_score},最低分:{min_score} 不及格人数:{count}")

def main():                     # 主菜单循环
    print("=====学生成绩管理系统====")
    print("请输入对应数字进行操作:")
    while True:
        print("\n1. 添加学生（学号、姓名、成绩）")
        print("2. 查看所有学生")
        print("3. 按学号查询单个学生")
        print("4. 统计：平均分 / 最高分 / 最低分 / 不及格人数")
        print("5. 退出")
        choice=int(input("输入你的选择(1~5)"))
        match choice:
            case 1:
                add_student(students)
            case 2:
                show_all(students)
            case 3:
                find_student(students)    
            case 4:
                show_stats(students)
            case 5:
                print("已退出")
                break
            case _:
                print("输入错误")

#调用学生成绩管理系统函数
main()
