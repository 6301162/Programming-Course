#Q1 Lists - Removing duplicates and sorting
def remove_duplicates_and_sort(numbers):
  return sorted(list(set(numbers))) #remove duplicates, then sort

numbers = [1, 2, 4, 3, 2]     #list with duplicates

print(remove_duplicates_and_sort(numbers)) #print the sorted list without including duplicates


#Q2 Single-Dimensional Arrays - Cummulative sum
def cummulative_sum(numbers):
    result = []    #create an empty list to store the cummulative sums
    total = 0      #start total at 0
    for num in numbers:
       total += num            #add the number to the total
       result.append(total)    #add the new total to the list
    return result

numbers = [3, 4, 5, 6, 7]
print(cummulative_sum(numbers))


#Q3 Slicing - extracting Every Nth Element:
def extract_every_nth(numbers, n):
  result = numbers[n-1::n]     #take every nth element from the list (starting at n-1)
  return result                

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]    #number list
n= int(input("Enter the value of n:"))    #ask user to enter the value of n
print(extract_every_nth(numbers, n))     #show the elements that appear every nth position


#Q4 Arithmetic Operations with Arrays - Dot product:
def dot_product(list1, list2):
  total = 0        #start total at 0
  for i in range(len(list1)):       #go through each position in the list
       total += list1[i]*list2[i]   #multiply the matching numbers and add it to the total
  return total

list1 = [3, 4, 5]
list2 = [5, 6, 7]

print(dot_product(list1, list2))


#Q5 Arithmetic operations with Arrays - Matrix multiplication
def matrix_multiply(A, B):
    result = [] #begin with an empty list for the final matrix
    for i in range(len(A)):   #go through each row of A
       row = []               #create a new row for the result
       for j in range(len(B[0])):   #go through ech row of B
         total = 0
         for k in range(len(B)):    #mulitply and add all matching elements
             total += A[i][k] * B[k][j]
         row.append(total)         #add the total to the row
         result.append(row)        #add row to the result matrix
    return result

A = [
[1, 2, 3],
[4, 5, 6]
]

B = [
[7, 8],
[9,10],
[11, 12]
]

print(matrix_multiply(A, B))