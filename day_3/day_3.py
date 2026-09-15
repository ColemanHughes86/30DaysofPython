import math
'''
age = 15
print(f'Your age is {age}')

height = 5.67
print(f'Your height is {height} feet tall.')

complex = 8 +16j
print(complex)

base = float(input("Enter base: "))
height_triangle = float(input('Enter height: '))
area = 0.5 * height_triangle * base

print(f'The area of the triangle is {area}')



side_a = int(input('What is the length of the first side: '))
side_b = int(input('What is the length of the second side: '))
side_c = int(input('What is the length of the third side: '))

perimeter= side_a + side_b + side_c
print(perimeter)

length = int(input('What is the length of the rectangle: '))
width = int(input('What is the width of the rectangle: '))
area = length * width
perimeter = (length * 2) + (width * 2)

print(area)
print(perimeter)


radius = float(input("What is the radius: "))
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print(area)
print(circumference)

m=2
b=-2

slope = m
y_intercept = b
x_intercept = -b/m
print(slope)
print(y_intercept)
print(x_intercept)

y2=10
y1=2
x2 = 6
x1 = 2
slope = (y2-y1)/(x2-x1)
print(slope)

euclidean_distance = math.sqrt(((y2-y1)**2)+((x2-x1)**2))
print(euclidean_distance)


answer = len('python') > len('dragon')
print(answer)


answer = 'on' in (('python') and ('dragon'))
print(answer)


sentence = 'jargon'  in 'I hope this course is not full of jargon'
print(sentence)

answer = 'on' not in (('python') and ('dragon'))
print(answer)

length = str(len('python'))
print(length)


number = int(input('Enter a number: '))
even = number % 2 == 0
print(f'The number {number} being even is {even}')

is_true = 7//3 == int(2.7)
print(is_true)


type = type('10') == type(10)
print(type)


num = int(float('9.8')) == (10)
print(num)


hours = int(input('Enter hours: '))
rph = int(input('Enter rate per hours: '))
days_per_week = int(input('How many days do you work per week: '))
pay = hours * rph * days_per_week
print(f'Your pay is {pay} per week')


years = int(input('Enter number of years you have lived'))
while years > 100:
    years = int(input('Enter number of years you have lived(pick a number less than 100)'))
else:
    seconds = years * 31,536,000
    print(f'You have live for {seconds} seconds')
'''
