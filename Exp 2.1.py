#2.1)Implement a python script to compute distance between two points taking inp from the user (Pythagorean Theorem).
import math
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print('The distance between',(x1,y1),'and',(x2,y2),'is',round(distance,2))
'''
Output
Enter x1: 15
Enter y1: 6
Enter x2: 20
Enter y2: 3
The distance between (15,6) and (20,3) is 5.83
'''
