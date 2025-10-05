import random

"""
Create list of 100 random numbers from 0 to 1000
"""

# declare list variable
numbers_list = []
for i in range(100): # for loop from 0 to 99 to create list with 100 elements
    numbers_list.append(random.randint(0, 1000)) # add random integer number from 0 to 1000 into numbers_list list using randint() function from random module

"""
Sort list from min to max (without using sort())
"""

for i in range (len(numbers_list)):
    for j in range (i+1, len(numbers_list)):
        # I loop through all the elements of the numbers_list list. I check one by one whether the current list element i is greater than any of the following elements, and if so, I swap these elements.. This way, I get a sorted list in ascending order.
        if numbers_list[i] > numbers_list[j]:
            n = numbers_list[i]
            numbers_list[i], numbers_list[j] = numbers_list[j], n

"""
Calculate average for even and odd numbers
"""
# Declare list variables for even and odd numbers
even_list = []
odd_list = []
# Check each element of the list, if it is even, then add the element to the list with even elements, if not, then add it to the list with odd elements.
for element in numbers_list:
    if element % 2 == 0:
        even_list.append(element)
    else: odd_list.append(element)

# calculate the average value in lists with even and odd numbers
even_avg = sum(even_list)/len(even_list)
odd_avg = sum(odd_list)/len(odd_list)

"""
Print both average result in console
"""
# Print the calculated average values using the f' line.
print(f'Average of even numbers in a list: {even_avg}')
print(f'Average of odd numbers in a list: {odd_avg}')

