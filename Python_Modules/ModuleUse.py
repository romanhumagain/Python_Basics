'''
 first way to call module
import Module as m

print(m.sum(4 , 6)) # to call the function of Module
print(m.mul(2, 5))
'''

# second way to call module

from Module import sum
print(sum(3,5))