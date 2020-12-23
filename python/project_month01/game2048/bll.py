"""
    游戏核心逻辑控制器
"""
import random

class GameCoreController:
    def __init__(self):
        self.map = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
        self.list_zero = []

    def __count_zero(self):
        self.list_zero.clear()
        for i in range(0,len(self.map)):
            for j in range(0,len(self.map[i])):
                if self.map[i][j] == 0:
                    self.list_zero.append((i,j))

    def generate_new_num(self):
        self.__count_zero()
        if len(self.list_zero) == 0: return
        target_i,target_j = self.list_zero[random.randint(0, len(self.list_zero)-1)]
        target_num = 4 if random.randint(0, 9) == 0 else 2
        self.map[target_i][target_j] = target_num

    def __square_matrix_tranpose(self):
        for c in range(len(self.map) - 1):
            for r in range(c + 1, len(self.map)):
                self.map[r][c], self.map[c][r] = self.map[c][r], self.map[r][c]

    def __zero_to_end(self,list_line):
        """
        零元素移动到末尾
        思路：从后向前依次判断，如果是零元素，则删除后追加零。
        """
        list_line
        for i in range(len(list_line) - 1, -1, -1):
            if (list_line[i] == 0):
                del list_line[i]
                list_line.append(0)
        return list_line

    def __merge(self,list_line):
        """
        合并
        思路：
            判断如果相邻且相同则合并
        """
        for i in range(0, len(list_line) - 1):
            if (list_line[i] == list_line[i + 1]):
                list_line[i] *= 2
                del (list_line[i + 1])
                list_line.append(0)
        return list_line

    def move_left(self):
        for i in range(0, len(self.map)):
            list_merge = self.__zero_to_end(self.map[i])
            self.map[i] = self.__merge(list_merge)
        self.generate_new_num()

    def move_right(self):
        for i in range(0, len(self.map)):
            # 因为切片，所以创建了新列表（深拷贝）
            list_merge = self.map[i][::-1]
            list_merge = self.__zero_to_end(list_merge)
            new_line = self.__merge(list_merge)
            self.map[i][::-1] = new_line
        self.generate_new_num()

    # 5. 定义函数，将二维列表map中的元素向上移动
    def move_up(self):
        self.__square_matrix_tranpose()
        self.move_left()
        self.__square_matrix_tranpose()

    # 6. 定义函数，将二维列表map中的元素向下移动
    def move_down(self):
        self.__square_matrix_tranpose()
        self.move_right()
        self.__square_matrix_tranpose()

    def check_if_move_row(self):
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i]) - 1):
                if (self.map[i][j] == self.map[i][j+1]):
                    return True
        return False

    def check_if_move_col(self):
        self.__square_matrix_tranpose()
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i]) - 1):
                if (self.map[i][j] == self.map[i][j+1]):
                    self.__square_matrix_tranpose()
                    return True
        self.__square_matrix_tranpose()
        return False

    def check_if_over(self):
        self.__count_zero()
        if len(self.list_zero)==0 and self.check_if_move_row() == False and self.check_if_move_col() == False:
            print("Game Over !")
            return True
        return False
