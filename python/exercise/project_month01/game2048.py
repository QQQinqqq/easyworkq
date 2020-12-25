"""
    2048 核心算法
"""

list_merge = [2,0,0,2]
# 1. 定义函数，将list_merge中的零元素移动到末尾
def zero_to_end():
    """
    零元素移动到末尾
    思路：从后向前依次判断，如果是零元素，则删除后追加零。
    """
    for i in range(len(list_merge)-1,-1,-1):
        if(list_merge[i] == 0):
            del list_merge[i]
            list_merge.append(0)

# 2. 定义函数，将list_merge中的元素进行合并（相邻且相同）
def merge():
    """
    合并
    思路：
        将零元素后移
        判断如果相邻且相同则合并
    """
    zero_to_end()
    for i in range(0,len(list_merge)-1):
        if(list_merge[i] == list_merge[i+1]):
            list_merge[i] *= 2
            del(list_merge[i+1])
            list_merge.append(0)

# 3. 定义函数，将二维列表map中的元素向左移动
map = [
    [2,0,0,2],
    [2,4,4,2],
    [0,4,2,0],
    [2,0,2,0]
]

def move_left():
    global list_merge
    for line in map:
        list_merge = line
        merge()


# 4. 定义函数，将二维列表map中的元素向右移动
def move_right():
    global list_merge
    for line in map:
        #因为切片，所以创建了新列表（深拷贝）
        list_merge = line[::-1]
        print(list_merge)
        merge()
        line[::-1] = list_merge

def square_matrix_tranpose(matrix):
    for c in range(len(matrix) - 1):
        for r in range(c+1,len(matrix)):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

# 5. 定义函数，将二维列表map中的元素向上移动
def move_up():
    square_matrix_tranpose(map)
    move_left()
    square_matrix_tranpose(map)

# 6. 定义函数，将二维列表map中的元素向下移动
def move_down():
    square_matrix_tranpose(map)
    move_right()
    square_matrix_tranpose(map)

move_up()
print(map)