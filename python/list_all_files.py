#!/usr/bin/python
# -*- coding: UTF-8 -*-

def list_all_files(rootdir):
    import os
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
               _istext = path.find(".txt")
               if _istext != -1:
                  _files.append(path)
                  print(path)
                  print("\n")
    return _files
    
    
_fs = list_all_files('D:\\QIN')