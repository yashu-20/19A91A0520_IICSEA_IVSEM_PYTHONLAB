'''
2.2) Implement a python script add.py that takes 2 number as command line arguments and perform arithmetic operations on them
'''
import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print('Sum',(num1+num2))
print('Difference',(num1-num2))
print('Product',(num1*num2))
print('Division',(num1//num2))
print('Modulus',(num1%num2))

'''
Output
E:\python programs\lab programs>python Exp2.2.py 20 20
Sum 40
Difference 20
Product 400
Division 1
Modulus 0
'''
