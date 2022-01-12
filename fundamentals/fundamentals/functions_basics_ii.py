#countdown Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
    decrease = []
    for i in range (num, -1, -1):
        decrease.append(i)
    return decrease

print(countdown(5))
print(countdown(10))

#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_return(list):
    print(list[0])
    return list[1]

print (print_return([10,20]))

# #First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(list):
    print(list[0])
    print(len(list))
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5,6]))

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def greater_than_second(list):
    if (len(list) < 2):
        return "False"
    else:
        newList = []
        for i in range (0,len(list),1):
            if(list[i] > list[1]):
                newList.append(list[i])
            else:
                continue
        # print(newList)
        # print(len(newList))
        return(f"The values greater than the second value of the list is : "+ str(newList) + " and it has " + str(len(newList)) + " value(s)")

print(greater_than_second([1]))
print(greater_than_second([1,2,3,4,5,6]))
print(greater_than_second([0,20,46,0]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def this_that(size, value):
    newList = []
    for i in range (0,size):
        newList.append(value)
    return newList

print(this_that(2,7))
print(this_that(4,1))
print(this_that(6,7))

