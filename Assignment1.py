# # #TASK1
def median_of_numbers(num1, num2, num3):
  sum =(num1 + num2+ num3)
  median=sum - min(num1, num2, num3) - max(num1, num2, num3)
  return median

num1=float(input('Enter the first number: '))
num2=float(input('Enter the second number: '))
num3=float(input('Enter the third number: '))

median=median_of_numbers(num1, num2, num3)

print(f' The median of the numbers are {median}')

# # #TASK2

def number_status(number):
  if number == 0:
    return('The number is zero ')
  elif number > 0:
    return('The number is positive ')
  else:
    return('The number is negative ')

number=float(input('Enter your number: '))

value=number_status(number)

print(value)


# # #TASK3

num=1
while num < 5:
  print(num*'*')
  num=num+1


def star_shape(rows):
  for i in range(1, rows + 1):
    print('*' * i)

rows=int(input('Enter the amount of rows: '))

star_shape(rows)


# Task 4
def count_multiples_of_3(limit):
  num=1
  while num <= limit:
     if num % 3 == 0:
       print('Multiple of 3')
     else:
       print(num)
     num+=1

limit=int(input('what number would you like to count up until? '))

count_multiples_of_3(limit)



#task 5

def sum_even_numbers(start, end):
 total=0
 for num in range(start, end+1):
   if num %2 == 0:
    total+=num
 return total


print(sum_even_numbers(1,10))