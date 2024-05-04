# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 11:43:09 2021

@author: admin
"""

a=float(input('請輸入依成績'))
if ((a>=90)and(a<=100)):
    print('%5.2f 分成績為優等' %(a))
elif ((a>=80)and(a<90)):
     print('%d 分成績為甲等' %(a))
else :
     print('您輸入的成績分數不在正常範圍內')
     