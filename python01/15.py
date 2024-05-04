# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 01:23:39 2021

@author:黃薇臻
"""

a=int(input('請輸入西元年:'))
if (a%100!=0) and (a%4==0):
    print('西元%d年為閏年' %(a))
elif (a%100==0) and (a%400==0):
    print('西元%d年為閏年' %(a))
else:
    print('西元%d不為閏年' %(a))    
    