'''
Aim
To write a Python program to demonstrate hierarchical inheritance, where two child classes inherit the properties and methods of a single parent class.
Algorithm
1. Start the program.
2. Create a parent class a with a method one().
3. Create a child class b that inherits from class a and define method two().
4. Create another child class c that inherits from class a and define method three().
5. Create an object of class b and call the methods one() and two().
6. Create an object of class c and call the methods one() and three().
7. Display the output.
8. Stop the program.'''


class a:
    def one(self):
        print("\nPARENT CLASS A")

class b(a):
    def two(self):
        print("\nCHILD CLASS B DERIVED FROM A")

class c(a):
    def three(self):
        print("\nCHILD CLASS C DERIVED FROM A")

obj = b()
obj.one()
obj.two()

obj = c()
obj.one()
obj.three()

"""
Output:
PARENT CLASS A

CHILD CLASS B DERIVED FROM A

PARENT CLASS A

CHILD CLASS C DERIVED FROM A
"""
