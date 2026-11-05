'''
Aim
To write a Python program to demonstrate various list operations such as length, append, sorting, extending, indexing, searching, inserting, slicing and removing elements.
Algorithm
1. Start.
2. Create a list named num containing the elements 12, 32, 15, 24, 53 and 50.
3. Display the original list.
4. Find and display the length of the list using len().
5. Add 100 to the end of the list using append().
6. Sort the list in ascending order using sort().
7. Sort the list in descending order using sort(reverse=True).
8. Create a new list containing 11, 22, 33 and 44.
9. Add the new list to the original list using extend().
10. Display the element at index 3 using indexing.
11. Find the position of 100 using index().
12. Insert 99 at the second position using insert().
13. Display elements from index 2 to 5 using slicing.
14. Remove 100 from the list using remove().
15. Display the final list.
16. Stop.
'''


num=[12,32,15,24,53,50]

print("ORIGINAL LIST: ",num)

print("LENGTH: ", len(num))

print("APPEND (100): ")
num.append(100)
print(num)

print("SORTED ASC: ")
num.sort()
print(num)

print("SORTED DESC: ")
num.sort(reverse=True)
print(num)

new=[11,22,33,44]
num.extend(new)
print("EXTENDED LIST: ",num)

print("INDEX[3]: ",num[3])

print("POSITION OF 100: ",num.index(100))

print("INSERT 99 at 2nd position: ")
num.insert(1,99)
print(num)

print("SLICING: ", num[2:6])

num.remove(100)
print("REMOVE 100:", num)


'''
OUTPUT

ORIGINAL LIST:  [12, 32, 15, 24, 53, 50]
LENGTH:  6
APPEND (100):
[12, 32, 15, 24, 53, 50, 100]

SORTED ASC:
[12, 15, 24, 32, 50, 53, 100]

SORTED DESC:
[100, 53, 50, 32, 24, 15, 12]

EXTENDED LIST:
[100, 53, 50, 32, 24, 15, 12, 11, 22, 33, 44]

INDEX[3]:  32
POSITION OF 100:  0

INSERT 99 at 2nd position:
[100, 99, 53, 50, 32, 24, 15, 12, 11, 22, 33, 44]

SLICING:  [53, 50, 32, 24]

REMOVE 100: [99, 53, 50, 32, 24, 15, 12, 11, 22, 33, 44]
'''
