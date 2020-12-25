"""
    迭代器
    目的：迭代自定义对象
"""
class SkillIterator():
    def __init__(self,data):
        self.__data=data
        self.__count=-1

    def __next__(self):
        self.__count += 1
        if(self.__count > len(self.__data)-1):
            raise StopIteration
        return self.__data[self.__count]

class SkillManager:
    count = 0
    def __init__(self):
        self.__skills=[]
    def add_skill(self,skill):
        self.__skills.append(skill)

    def __iter__(self):
        return SkillIterator(self.__skills)

manager = SkillManager()
manager.add_skill("skill a")
manager.add_skill("skill b")
manager.add_skill("skill c")

for item in manager:
    print(item)