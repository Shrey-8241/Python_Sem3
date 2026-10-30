class inventory:

    def GetInv(self):
        print("\nINPUT ITEM NAME")
        self.item=input("ENTER NAME:")
    def GetPrice(self):
        print("\nINPUT ITEM PRICE")
        self.price=int(input("ENTER PRICE:"))
    def GetQty(self):
        print("\nINPUT ITEM PRICE")
        self.qty=int(input("ENTER QUANTITY:"))

class total(inventory):
    def ans(self):
        print("TOTAL COST OF", self.item,"=",self.price * self.qty)

obj=total()
obj.GetInv()
obj.GetPrice()
obj.GetQty()
obj.ans()
        

