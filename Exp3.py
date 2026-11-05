'''
Aim
To write a Python program to demonstrate various string operations such as length, uppercase, lowercase, slicing, indexing, searching, replacing, concatenation and stripping.
Algorithm
1. Start.
2. Declare a string variable S and initialize it with "PYTHON PROGRAMMING     ".
3. Display the original string.
4. Find and display the length of the string using len().
5. Convert and display the string in uppercase using upper().
6. Convert and display the string in lowercase using lower().
7. Extract and display characters from index 1 to 6 using slicing.
8. Display the character at index 6 using indexing.
9. Find and display the position of "PROG" using find().
10. Replace "PYTHON" with "DBMS" using replace().
11. Check whether "COMP" is present in the string using the in operator.
12. Concatenate the string with " LAB" and display the result.
13. Remove leading and trailing spaces using strip() and display the stripped string and its length.
14. Stop.
'''


S="PYTHON PROGRAMMING     "
print ("OG STRING: ",S)
print("LENGTH: ",len(S))
print("UPPER CASE: ",S.upper())
print("LOWER CASE: ",S.lower())
print("SLICING: ",S[1:7])
print("INDEXING: ",S[6])
print("POSITION OF 'PROG': ",S.find('PROG'))
print("REPLACE PYTHON WITH DBMS: ",S.replace("PYTHON","DBMS"))
print("CHECK WORD: ","COMP" in S)
print("CONCATENATION: ",S + ' LAB')
print("STRIP: ",S.strip(),len(S))

'''
OG STRING:  PYTHON PROGRAMMING     
LENGTH:  23
UPPER CASE:  PYTHON PROGRAMMING     
LOWER CASE:  python programming     
SLICING:  YTHON 
INDEXING:   
POSITION OF 'PROG':  7
REPLACE PYTHON WITH DBMS:  DBMS PROGRAMMING     
CHECK WORD:  False
CONCATENATION:  PYTHON PROGRAMMING      LAB
STRIP:  PYTHON PROGRAMMING 23
'''
