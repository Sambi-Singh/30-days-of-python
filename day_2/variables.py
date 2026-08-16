# Day 2: 30 days of python programming
import math
first_name = 'Sambi'
last_name = 'Singh'
full_name = 'Sambi Singh'
country = 'USA'
city = 'Irving'
age = 22
year = '2026'
is_married = False
is_true = True
is_light_on = True

fruit_name, fruit_color, fruit_price, is_fruit_ripe = 'Apple', 'Red', 1.30, True

#print(fruit_name)
#print(is_light_on)

#find data type of all variables using type()
print(type(first_name), ' ', type(last_name), ' ', type(full_name), ' ', type(country), type(city), ' ', type(age), ' ', type(is_married), ' ', type(is_true), type(is_light_on), ' ', type(fruit_name), ' ', type(fruit_color), ' ', type(fruit_price), ' ', type(is_fruit_ripe))
print(len(first_name))
print('The length of my first name is ', len(first_name), ' and the length of my last name is ', len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

#12. calculate area of circle, given radius 30 m
#i. find area
area_of_circle = round((math.pi) * 30 **2, 2)
print('The area of the circle is:', area_of_circle, 'square meters')

#ii. find circumference
circum_of_circle = round(2 * math.pi * 30, 2)
print('The circumference of the circle is:', circum_of_circle, 'meters')

#iii. calculate area again but using user input for getting radius
user_radius = input('Please enter the radius: ')
area_of_circle = round((math.pi) * float(user_radius) **2, 2)
print('The area of the circle (with users radius) is:', area_of_circle, 'square meters')

first_name = input('What is your first name?: ')
last_name = input('What is your last name?: ')
country = input('Which country do you live in?: ')
age = input('How old are you?: ')

print('Hello!', first_name, last_name, 'I hope your summer is going well!', country, 'Seems like such a cool place! Would love to visit one day :D', age, '?? Wow you are still so young too!')
