# Basic - Print all integers from 0 to 150.

print("Basics")
for count in range (0,151):
    print(count)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
print("Multiples of Five")
for five in range (5,1001, 5):
    print(five)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

print("Counting, the Dojo Way")
for divideFive in range (0, 151):
    if divideFive % 10 == 0:
        print("Coding Dojo")
    elif divideFive % 5 ==0:
        print("Coding")
    else:
        print(divideFive)


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
print("Whoa That Sucker's Huge")

total = 0
for odd in range (0,500001):
    if odd % 2 ==1 or odd %2 !=0:
        total += odd
print(total)

# sum = 0
# for i in range(1,500001,2):
#     sum += i
# print(sum)


# odd = 0
# while odd <= 5000000:
#     if odd % 2 ==1:
#         print(odd)

# total = sum(odd)
# print(total)

# # Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
print("Countdown by Fours")
positive = 2018
while positive >= 0:
    print(positive)
    positive -= 4

# for i in range(2018,0,-4):
#     print(i)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

print("Flexible Counter")
low = 2
high = 9
mult = 3

for flexible in range (low, high+1):
    if flexible % mult == 0:
        print(flexible)