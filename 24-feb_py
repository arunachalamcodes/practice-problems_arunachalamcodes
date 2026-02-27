# ================================================
# Python List Practice Programs
# Author: Your Name
# Description: Common list operations, list comprehension,
#              digit sum, deletion, min, sum, avg, filtering
# ================================================

# ------------------------------------------------
# 1. Cubes using List Comprehension
# ------------------------------------------------

cubes = [i**3 for i in range(101)]
print("Cubes from 0 to 100:")
print(cubes)


# ------------------------------------------------
# 2. Sum of Digits of Each Number in List
# ------------------------------------------------

nums = [123, 321, 456]

digit_sum = [sum(int(d) for d in str(n)) for n in nums]
print("\nSum of digits of each number:")
print(digit_sum)


# ------------------------------------------------
# 3. Delete Elements from List using pop()
# ------------------------------------------------

a = [[123], [321], [111], [555], [888]]
loop = 1

while loop:
    print("\nCurrent List:", a)
    x = int(input("Enter the index to delete: "))

    if 0 <= x < len(a):
        deleted = a.pop(x)
        print(f"{deleted} deleted from index {x}")
    else:
        print("Invalid index")

    loop = int(input("Enter 1 to continue, 0 to exit: "))


# ------------------------------------------------
# 4. Minimum Value in List (Manual Method)
# ------------------------------------------------

a = [[123], [321], [111], [555], [888]]

minimum = a[0]
for i in a:
    if i < minimum:
        minimum = i

print("\nMinimum element:", minimum)


# ------------------------------------------------
# 5. Sum of Digits (Manual Method)
# ------------------------------------------------

a = [123, 321, 111, 555, 888]

print("\nManual sum of digits:")
for i in a:
    temp = i
    total = 0

    while temp > 0:
        total += temp % 10
        temp //= 10

    print(f"{total} is the sum of digits of {i}")


# ------------------------------------------------
# 6. Sum & Average of List
# ------------------------------------------------

import statistics

a = [1, 2, 3, 4, 5]

print("\nUsing built-in sum():", sum(a))
print("Using statistics.mean():", statistics.mean(a))

# Manual sum
s = 0
for i in a:
    s += i
print("Manual sum:", s)

# Manual average
print("Manual average:", s / len(a))


# ------------------------------------------------
# 7. Check Element Exists in List
# ------------------------------------------------

a = [0, 1, 2, 3, 4]

print("\nCheck if 2 exists in list:")
print(2 in a)


# ------------------------------------------------
# 8. Count Occurrences of Each Element
# ------------------------------------------------

a = [0, 1, 1, 1, 3]

print("\nCount of each element:")
for i in set(a):
    print(f"{i} occurs {a.count(i)} times")


# ------------------------------------------------
# 9. Remove Multiple Elements from List
# ------------------------------------------------

a = [10, 20, 30, 40, 50, 60]
remove = [10, 30, 40]

filtered = [x for x in a if x not in remove]

print("\nList after removing elements:")
print(filtered)
