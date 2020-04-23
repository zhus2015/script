#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName:计算x的n此房.py
# @Author:   
# @Date:2020/4/23

def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2,5))