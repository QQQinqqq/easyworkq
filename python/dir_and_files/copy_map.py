#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil

dir_010="D:\\QIN\\exercise\\练习区\\sdk_qin\\SPC057B010"
list = os.listdir(dir_010) #列出文件夹下所有的目录与文件
#list = ["SPC057B010","SPC057B011","SPC057B012","SPC057B013","SPC057B014","SPC057B015","SPC057B016","SPC057B017","SPC057B018","SPC057B019","SPC057B020","SPC057B021","SPC057B022","SPC057B023","SPC057B024","SPC057B025","SPC057B026","SPC057B027","SPC057B028","SPC057B029","SPC057B030","SPC057B031","SPC057B032","SPC057B033","SPC057B034","SPC057B035","SPC057B036","SPC057B037","SPC057B038","SPC057B039","SPC057B040","SPC057B041","SPC057B042","SPC057B043","SPC057B044","SPC057B045","SPC057B046","SPC057B047","SPC057B048","SPC057B049","SPC057B050","SPC057B051","SPC057B052","SPC057B053","SPC057B054","SPC057B055","SPC057B056","SPC057B057","SPC057B058"]
for i in range(0,len(list)):
    if list[i] == "sdk_released":
        continue
    shutil.copytree(dir_010+"\\"+list[i]+"\\output\\mk_image\\image", dir_010+"\\上传_"+list[i])
    os.makedirs(dir_010+"\\上传_"+list[i]+"\\map")
    shutil.copyfile(dir_010+"\\"+list[i]+"\\output\\CCO\\bin\\123456_cco.map", dir_010+"\\上传_"+list[i]+"\\map\\123456_cco.map")
    shutil.copyfile(dir_010+"\\"+list[i]+"\\output\\STA\\bin\\123456_sta.map", dir_010+"\\上传_"+list[i]+"\\map\\123456_sta.map")
    shutil.copyfile(dir_010+"\\"+list[i]+"\\output\\NDM\\bin\\123456_ndm.map", dir_010+"\\上传_"+list[i]+"\\map\\123456_ndm.map")

os.rename(dir_010+"\\上传_sdk_beijing_real",dir_010+"\\北京_真实表")
os.rename(dir_010+"\\上传_sdk_beijing_virtual",dir_010+"\\北京_虚拟表")
os.rename(dir_010+"\\上传_sdk_beijing_virtual_099",dir_010+"\\北京_虚拟表_099")
os.rename(dir_010+"\\上传_sdk_csg_real",dir_010+"\\南网_真实表")
os.rename(dir_010+"\\上传_sdk_csg_virtual",dir_010+"\\南网_虚拟表")
os.rename(dir_010+"\\上传_sdk_csg_virtual_099",dir_010+"\\南网_虚拟表_099")
os.rename(dir_010+"\\上传_sdk_jiangsu_real",dir_010+"\\江苏_真实表")
os.rename(dir_010+"\\上传_sdk_jiangsu_virtual",dir_010+"\\江苏_虚拟表")
os.rename(dir_010+"\\上传_sdk_jiangsu_virtual_099",dir_010+"\\江苏_虚拟表_099")
os.rename(dir_010+"\\上传_sdk_std_real",dir_010+"\\国网_真实表")
os.rename(dir_010+"\\上传_sdk_std_virtual",dir_010+"\\国网_虚拟表")
os.rename(dir_010+"\\上传_sdk_std_virtual_099",dir_010+"\\国网_虚拟表_099")
