'''
Aim
To write a menu-driven Python program using if-elif-else statements to calculate an electricity bill based on the number of units consumed and display the applicable tariff rates.
Algorithm
1. Start.
2. Display the electricity bill calculator menu with three options:
   - Calculate Electricity Bill
   - View Tariff Rates
   - Exit
3. Accept the user's choice.
4. If the choice is 1:
   - Accept the number of electricity units consumed.
   - Check whether the units are less than 0. If true, display "Invalid Input".
   - If units are less than or equal to 100, calculate the bill at ₹2 per unit.
   - If units are between 101 and 200, charge ₹2 for the first 100 units and ₹3 for the remaining units.
   - If units are above 200, charge ₹2 for the first 100 units, ₹3 for the next 100 units and ₹5 for the remaining units.
   - Display the total electricity bill.
5. If the choice is 2, display the electricity tariff rates.
6. If the choice is 3, display "Thank You!".
7. If the choice is invalid, display "Invalid Choice".
8. Stop.
'''

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
    elif units <= 200 and units >100:
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

'''
OUTPUT

1. Calculate Electricity Bill
2. View Tariff Rates
3. Exit
Enter your choice: 1
Enter units consumed: 230
Electricity Bill: Rs. 650
'''
