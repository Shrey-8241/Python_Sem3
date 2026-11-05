'''
Aim
To write a Python program to demonstrate different types of operators such as identity, membership, assignment, arithmetic, bitwise and logical operators.
Algorithm
1. Start.
2. Initialize variables a = 10, b = 20 and c = a.
3. Demonstrate identity operators using is and is not.
4. Demonstrate membership operators using in to check whether characters are present in a string.
5. Initialize x = 10.
6. Perform assignment operations using +=, -=, *=, /=, //=, %=, and **=.
7. Perform arithmetic operations such as addition, subtraction, division, multiplication and modulus.
8. Initialize y = 12 and q = 10.
9. Perform bitwise operations using &, |, ^, ~, << and >>.
10. Perform logical operations using and, or and not.
11. Display all the results.
12. Stop.
'''

print("IDENTITY OPERATORS\n")
a=10
b=20
c=a
print (a is not b)
print (a is c)

print("\nMEMBERSHIP OPERATORS\n")
print('a' in 'apple')
print('b' in 'apple')

print("\nASSIGNMENT OPERATORS\n")
x=10
print("X=",x)
x+=3
print('x+=3',x)
x-=3
print('x-=3',x)
x*=3
print('x*=3',x)
x/=3
print('x/=3',x)
x//=3
print('x//=3',x)
x%=3
print('x%=3',x)
x**=3
print('x**=3',x)

print("\nARITHMETIC OPERATORS\n")
print("a+b ",a+b)
print("a-b ",a-b)
print("a/b ",a/b)
print("a*b ",a*b)
print("a%b ",a%b)


print("\nBITWISE OPERATORS\n")
y = 12
q = 10

print(y & q)
print(y | q)
print(y ^ q)   
print(~y)   
print(y << 2)
print(y >> 2)

print("\nLOGICAL OPERATORS\n")
print(y and q)
print(y or q)
print(not q) 

'''
OUTPUT

IDENTITY OPERATORS

True
True

MEMBERSHIP OPERATORS

True
False

ASSIGNMENT OPERATORS

X= 10
x+=3 13
x-=3 10
x*=3 30
x/=3 10.0
x//=3 3.0
x%=3 0.0
x**=3 0.0

ARITHMETIC OPERATORS

a+b  30
a-b  -10
a/b  0.5
a*b  200
a%b  10

BITWISE OPERATORS

8
14
6
-13
48
3

LOGICAL OPERATORS

10
12
False
'''
