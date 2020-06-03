#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil

#创建文件夹
def mkdir(path):
    # 移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    path=path.strip()
    # 删除字符串末尾的\\
    path=path.rstrip("\\")
  
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
  
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
  
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False


#复制文件夹
def copy_files(source_dir, target_dir):
    shutil.copytree(source_dir, target_dir)
    print('copy dir finished!')


if __name__ == "__main__":
    # 调用函数
    #mkdir("d:\\123\\")
    shutil.copytree("D:\\exercise", "d:\\123\\")
