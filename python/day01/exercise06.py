"""
    封装 -- 私有成员
"""

class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if 20 <= value <= 50:
            self.__age = value
        else:
            raise Exception("invalid")
    # 类变量，先创建
    #age = property(get_age,set_age)

w01 = Person("Tom",25)
w02 = Person("Marry",28)
print(w01.__dict__)