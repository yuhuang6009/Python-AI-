#练习：学生成绩管理系统-类表示
# 一个学生 = 一个字典
#student = {"id": "2024001", "name": "小明", "score": 85}
class StudentManager:
    def __init__(self):
        self.students=[]
    def add_student(self):
        self.student={}
        self.student["id"]=input("学号：")
        for stu in self.students:
            if self.student["id"]==stu["id"]:
                print("学号已存在")
                break
        else:
            self.student["name"]=input("姓名：")
            self.student["score"]=int(input("成绩："))
            self.students.append( self.student)

    def show_all(self):         # 查看所有
        for i in self.students:
            print(i)

    def find_student(self):     # 按学号查找
        self.id_student=input("输入学生学号:")
        for stu in self.students:
            if self.id_student==stu["id"]:
                print(stu)
                break
        else:
            print("查找不到该学生")

    def show_stats(self):       # 统计
        if len(self.students)==0:
            print("还没有学生，请先添加")
        else:
            sum=0;ave=0;max_score=0;min_score=0;count=0
            max_score = self.students[0]["score"]  # 先拿第一个当基准
            min_score = self.students[0]["score"]
            for stu in self.students:
                sum+=stu["score"]
                ave=sum/len(self.students)
                if stu["score"] > max_score:
                    max_score = stu["score"]
                if stu["score"] < min_score:
                    min_score = stu["score"]
                if stu["score"]<60:
                    count+=1
            print(f"平均分:{ave},最高分:{max_score},最低分:{min_score} 不及格人数:{count}")

    def main(self):                     # 主菜单循环
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
                    self.add_student()
                case 2:
                    self.show_all()
                case 3:
                    self.find_student()    
                case 4:
                    self.show_stats()
                case 5:
                    print("已退出")
                    break
                case _:
                    print("输入错误")
            

if __name__=='__main__':
    studentmanager=StudentManager()
    studentmanager.main()