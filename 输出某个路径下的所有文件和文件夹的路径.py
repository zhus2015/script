#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName:输出某个路径下的所有文件和文件夹的路径.py
# @Author:   
# @Date:2020/4/23


import os

def print_dir():
    filepath = input("请输入一个路径:")
    if filepath == "":
        print("请输入正确的路径")
    else:
        for i in os.listdir(filepath):
            print(os.path.join(filepath,i))

print(print_dir())