#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName:冒泡排序.py
# @Author:   
# @Date:2020/4/23


lis = [56,12,1,8,23,5,7,9,23,8,98,254,-45]

def sortport():
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    return lis


if __name__ == '__main__':
    print(sortport())