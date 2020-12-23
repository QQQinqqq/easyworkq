"""
    步骤一：
        数据模型类：StudentModel
            数据：姓名 name，年龄 age，成绩 score，编号 id，
        逻辑控制类：StudentManagerController
            数据：学生列表 __stu_list
            行为：获取列表 stu_list，
                添加学生 add_student
                删除学生 remove_student
                根据成绩进行升序排列
"""

class StudentModel:
    """
        学生数据模型类
    """
    def __init__(self, name="", age=0, score=0,id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    """
        学生管理控制器：主要负责业务逻辑处理
    """
    count_id = 1000
    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self,name="",age=0,score=0):
        new_item = StudentModel(name,age,score,StudentManagerController.count_id)
        self.__stu_list.append(new_item)
        StudentManagerController.count_id += 1

    def remove_student(self,id=0):
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
        return False

    def update_student(self,id=0,name="",age=0,score=0):
        for item in self.__stu_list:
            if item.id == id:
                item.name=name
                item.age = age
                item.score = score
                return True
        return False

    def order_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for j in range(i+1,len(self.__stu_list)):
                if self.__stu_list[i].score > self.__stu_list[j].score:
                    self.__stu_list[i], self.__stu_list[j] = self.__stu_list[j], self.__stu_list[i]

class StudentManagerView:
    """
        学生管理视图：主要负责界面逻辑
    """
    def __display_menu(self):
        print("1)添加")
        print("2)查看")
        print("3)删除")
        print("4)修改")
        print("5)排序")
        print("6)退出")

    def __select_menu(self,stru_list):
        item = input("input:")
        if item == "1":
            name = input("name:")
            age = input("age:")
            score = input("score:")
            stru_list.add_student(name,age,score)
        elif item == "2":
            stru_list.stu_list
            for i in student_ctrl.stu_list:
                print(i.id, i.name, i.age, i.score, sep="\t")
        elif item == "3":
            id = input("id:")
            stru_list.remove_student(id)
        elif item == "4":
            id = input("id:")
            name = input("name:")
            age = input("age:")
            score = input("score:")
            stru_list.update_student(id,name, age, score)
        elif item == "5":
            stru_list.order_by_score
        elif item == "6":
            return 1
        return 0


    def main(self,stru_list):
        while True:
            self.__display_menu()
            re = self.__select_menu(stru_list)
            if re == 1:
                break

student_ctrl = StudentManagerController()
view = StudentManagerView()
view.main(student_ctrl)