#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName:输出某个路径及其子目录下的所有文件路径.py
# @Author:   
# @Date:2020/4/23

import os

def show_dir(filepath):
    for i in os.listdir(filepath):
        path = (os.path.join(filepath,i))
        print(path)
        if os.path.isdir(path):
            show_dir(path)

show_dir("C:\Program Files\internet explorer")