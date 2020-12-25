import bll
import os

if __name__ == "__main__":
    gcc = bll.GameCoreController()
    gcc.generate_new_num()
    gcc.generate_new_num()

    while True:
        os.system("clear")
        for i in gcc.map:
            for j in i:
                print(j,end="\t")
            print( end="\n")
        print( )
        direction = input("滑动（asdw）：")
        if direction == "a":
            gcc.move_left()
            if(gcc.check_if_over()):break
        elif direction == "s":
            gcc.move_down()
            if (gcc.check_if_over()): break
        elif direction == "d":
            gcc.move_right()
            if (gcc.check_if_over()): break
        elif direction == "w":
            gcc.move_up()
            if (gcc.check_if_over()): break
        else:
            print("wrong input")