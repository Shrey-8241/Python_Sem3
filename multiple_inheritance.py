class a:
    def one(self):
        print("\nPARENT CLASS A")
class b:
    def two(self):
        print("\nPARENT CLASS B")
class c(a,b):
    def three(self):
        print ("\nCHILD CLASS DERIVED FROM A & B")
obj=c()
obj.one()
obj.two()
obj.three()
