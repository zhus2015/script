#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName:输出某个路径及其子目录下所有以.html为后缀的文件.py
# @Author:   
# @Date:2020/4/23


import os

def print_dir(filepath):
    for i in os.listdir(filepath):
        path = (os.path.join(filepath,i))
        if os.path.isdir(path):
            print(path)
        if path.endswith(".exe"):
            print(path)

print_dir("C:\Program Files\internet explorer")