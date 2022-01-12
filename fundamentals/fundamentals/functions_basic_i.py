#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

# #print 5

# #2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# # not defined number_of days functions is not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#print 5 -> only one return value thus after line 15 it doesnt matter


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#print 5; 10 is only for us and without return, function will only return the return value


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#return 5 and than none because by CALLing x we returned the value of 5, but print(x) does not CALL the function


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#print 3 print 5 + will concatenate two values not add ^^^^^

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#print "2" and "5" with no space so 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#return 100 and than 10 becasue it meets the else statement

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#prints 7 then 14, then 7+ 14 which is 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#returns 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#500, skips the function cuz not called yet, 500, function is called so 300, then 500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#500, 500, 300, 500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#500, 500, 300, 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#1, 3, 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#1, 3, 5, 10