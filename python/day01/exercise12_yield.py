"""
    迭代器
    目的：迭代自定义对象
"""
class SkillManager:
    count = 0
    def __init__(self):
        self.__skills=[]
    def add_skill(self,skill):
        self.__skills.append(skill)

    def __iter__(self):
        print("ready")
        yield self.__skills[0]
        print("ready")
        yield self.__skills[1]
        print("ready")
        yield self.__skills[2]

manager = SkillManager()
manager.add_skill("skill a")
manager.add_skill("skill b")
manager.add_skill("skill c")

for item in manager:
    print(item)