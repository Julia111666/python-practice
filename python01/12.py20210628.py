# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 11:44:47 2021

@author: admin
"""

for i in range (1,10):
    print (i)
    
sum=0
for i in range (1,11):
        sum+=i  #sum=sum+i
        print('目前sum=%d' %(sum))
        
        print ('1加到10的結果為%d' %(sum))
        
sum_p=0
for i in range (1,11):
    if (i%2==0):
       sum_p+=i
       print (i,sum_p)

print ('1到10的偶數和為%d' %(sum_p))
        
        