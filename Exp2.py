print("\t=== ELECTRICITY BILL CALCULATOR ===")
print("1. Calculate Electricity Bill")
print("2. View Tariff Rates")
print("3. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    units = int(input("Enter units consumed: "))

    if units < 0:
        print("Invalid Input")
    elif units <= 100:
        bill = units * 2
        print("Electricity Bill: Rs.", bill)
    elif units <= 200:
        bill = 200 + (units - 100) * 3
        print("Electricity Bill: Rs.", bill)
    else:
        bill = 500 + (units - 200) * 5
        print("Electricity Bill: Rs.", bill)

elif choice == 2:
    print("First 100 units: Rs. 2/unit")
    print("Next 100 units: Rs. 3/unit")
    print("Above 200 units: Rs. 5/unit")

elif choice == 3:
    print("Thank You!")

else:
    print("Invalid Choice")
