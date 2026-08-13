
#Day 1 - exercise lvl 2: 
#-----------------------

#1. question 1. print python version number
import sys
print('Python version: ' + sys.version)

#2. operations on 3 and 4
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

#3. print strings
print('Sambi')
print('Singh')
print('United States of America')
print('I am enjoying 30 days of python')

#4. check data type of values printed
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Sambi'))
print(type('Singh'))
print(type('United States of America'))
print(" ")

#-----------------------
#Day 1 - exercise lvl 3: 
#-----------------------

#1. Write different numbers for python data types mentioend earlier

#numbers
print(25) # int
print(14.98) # float
print(3+10j) # complex --> x + yi format fyi

#data structures
print([10, 300, '20']) # list
print((199, 212, 2.2, 'Yo')) # tuple
print({'Dog': 'Woof', 'Cat': 'Meow', 0:'Zero!'}) # dict
print({100,100,100,'100'}) # set

#string
print('''Hugeeee block of texxxxtttttt, multiple lines long lmao!
      yesssssss :D''')

print(" ")

#2. Find the euclidean distance between (2,3) and (10,8)

# formula for two points: sqrt((x1-x2)^2 + (y1-y2)^2), trick! raise to power .5
print((((2-10)**2)+((3-8)**2))**0.5)


