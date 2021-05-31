'''
Implement a python script to count frequency of characters in a given string.
'''

input_str = input('Enter a string: ')

alphabet_count = {}

for character in input_str:
	alphabet_count[character] = alphabet_count.get(character,0) + 1


for key in sorted(alphabet_count.keys()):
	print('Count of {} is {}'.format(key,alphabet_count[key]))

  
'''
Output:
Enter a string: python
Count of h is 1
Count of n is 1
Count of o is 1
Count of p is 1
Count of t is 1
Count of y is 1
'''
