'''
Aim
To write a Python program to demonstrate various tuple operations and functions such as length, indexing, slicing, count, index, maximum, minimum and sum.
Algorithm
1. Start.
2. Create a tuple containing integer elements.
3. Display the original tuple.
4. Find and display the length of the tuple.
5. Access an element using indexing.
6. Extract elements using slicing.
7. Count the occurrence of an element using count().
8. Find the position of an element using index().
9. Display the maximum and minimum values using max() and min().
10. Calculate the sum of all elements using sum().
11. Sort the tuple and display the result.
12. Perform concatenation and repetition operations.
13. Stop.
'''


t = (12, 32, 15, 24, 53, 50)

print("ORIGINAL TUPLE: ", t)

print("LENGTH: ", len(t))

print("INDEX[2]: ", t[2])

print("SLICING: ", t[1:4])

print("COUNT OF 32: ", t.count(32))

print("POSITION OF 53: ", t.index(53))

print("MAXIMUM: ", max(t))

print("MINIMUM: ", min(t))

print("SUM: ", sum(t))

print("SORTED TUPLE: ", tuple(sorted(t)))

print("CONCATENATION: ", t + (60, 70))

print("REPETITION: ", t * 2)


'''
OUTPUT
ORIGINAL TUPLE:  (12, 32, 15, 24, 53, 50)
LENGTH:  6
INDEX[2]:  15
SLICING:  (32, 15, 24)
COUNT OF 32:  1
POSITION OF 53:  4
MAXIMUM:  53
MINIMUM:  12
SUM:  186
SORTED TUPLE:  (12, 15, 24, 32, 50, 53)
CONCATENATION:  (12, 32, 15, 24, 53, 50, 60, 70)
REPETITION:  (12, 32, 15, 24, 53, 50, 12, 32, 15, 24, 53, 50)
'''
