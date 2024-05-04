# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:57:59 2021

@author: USER
"""

a=float(input('請輸入國文成績'))
b=float(input('請輸入英文成績'))
c=float(input('請輸入數學成績'))
d=float(input('請輸入物理成績'))

print (a,b,c,d)

ans1=(a+b)/2
ans2=(c+d)/2
ans3=(a+b+c+d)/4
print(ans1,ans2,ans3)

print('文科的成績平均為:%5.2f分' %(ans1))
print('理科的成績平均為:%7.3f分' %(ans2))
print('平均為:%9.4f分' %(ans3))





