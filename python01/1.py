# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:32:15 2021

@author: USER
"""

a=int(input('請輸入一華氏溫度:'))
b=(a-32)*(5/9)
print ('華氏%d度等於攝氏%f度' %(a,b))

a=float(input('請輸入一攝氏溫度:'))
b=(a*(9/5))+32
print ('攝氏%f度等於華氏%f度' %(a,b))
