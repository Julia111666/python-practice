# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 11:30:11 2021

@author: admin
"""

#判斷所輸入的數值是否為二位數
num=int(input('請輸入一數值'))
a=((num>=100)and(num<=999))
print('%d 為三位數的邏輯判斷是 %s' %(num,a))
