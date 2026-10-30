class a:
    def one(self):
        print("\nPARENT CLASS A")
class b(a):
    def two(self):
        print("\nCHILD CLASS B DERIVED FROM A")
class c(a):
    def three(self):
        print ("\nCHILD CLASS C DERIVED FROM A")
obj=b()
obj.one()
obj=c()
obj.two()
obj.three()
