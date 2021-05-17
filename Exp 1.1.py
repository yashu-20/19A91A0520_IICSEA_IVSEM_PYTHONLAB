# Exp 1.1) Running Instructions in interactive interepreter and a Python script
>>> num = 20
>>> print(num)
20
>>> type(num)
<class 'int'>
>>> a = 20
>>> b = 30
>>> 
>>> result = a+b
>>> 
>>> print(result)
50
>>> 
>>> str1 = 'Hello World'
>>> 
>>> print(str1)
Hello World
>>> 
>>> type(str1)
<class 'str'>
>>> 
>>> type(type(str1))
<class 'type'>
>>> 
>>> len(str1)
11
>>> 
>>> 


#Python script to get bill amount
bill_amt = int(input('Enter bill amount: '))
discount = 0.0
if(bill_amt >= 1000):
	discount = 0.9
else:
	discount = 0.95
print('Final bill with discount:',(bill_amt*discount))

'''
Output
Sample test1
Enter bill amount: 1224
Final bill with discount: 1101.6
Sample test2
Enter bill amount: 530
Final bill with discount: 503.5
'''
