# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 10:16:07 2021

@author: admin


a=10
b=3
c=3.5
d=9.1
e='abcd'
f='efgh'


print(a,b)
print('第一個數值為%d,第二個數值為%d' %(a.b))
print('第一個數值為%f,第二個數值為%f' %(c.d))
print('第一個數值為%s,第二個數值為%s' %(e.f))

print('第一個數值為%1.2f,第二個數值為%1.4f,' %(c.d))


name="台北101"
height=508
print("%s的高度為%d公尺"%(name,height))

print()

building1="台北101大樓"
building2="杜拜的哈里發塔"
height=508
height=828.5
print("%10s的高度為%8d公尺",%(building1,height1))      #+10是靠右對齊
print("%-10s的高度為%8d公尺",%(building2,height2))     #-10是靠左對齊
print("%-10s的高度為%8.2f公尺",%(building2,height2))   

building="Taipei 101"
height=508.35
print("{0}的高度為{1}公尺" .format)(building,height))
print("{0:10s}的高度為{1:6.1f}公尺" .format)(building,height))
