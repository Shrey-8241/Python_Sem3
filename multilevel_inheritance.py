class a:
    def one(self):
        print("\nPARENT CLASS A")
class b(a):
    def two(self):
        print("\nCHILD CLASS B DERIVED FROM A")
class c(b):
    def three(self):
        print ("\nCHILD CLASS C DERIVED FROM B")
obj=c()
obj.one()
obj.two()
obj.three()
