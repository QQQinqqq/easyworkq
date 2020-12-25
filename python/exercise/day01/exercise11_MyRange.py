"""
    for item in MyRange(5):
        print(item)
"""
class MyRangeIterator():
    def __init__(self, max_number=0):
        self.__max_number = max_number
        self.__curr_number = -1

    def __next__(self):
        self.__curr_number += 1
        if self.__curr_number > self.__max_number-1:
            raise StopIteration
        return self.__curr_number

class MyRange():
    def __init__(self,max_number):
        self.__max_number = max_number
        
    def __iter__(self):
        return MyRangeIterator(self.__max_number)

for item in MyRange(99999999999):
    print(item)