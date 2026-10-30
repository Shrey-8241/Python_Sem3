'''
Aim
To write a Python program using the re module to check whether the entered input is a valid email ID or a 10-digit mobile number.
Algorithm
1. Start the program.
2. Import the re module.
3. Ask the user to enter an email ID or mobile number.
4. Create regular expression patterns for email and mobile number validation.
5. Use re.fullmatch() to check whether the input matches the email pattern.
6. If it matches, display "Valid Email ID".
7. Otherwise, check whether it matches the mobile number pattern.
8. If it matches, display "Valid Mobile No".
9. If neither pattern matches, display "Invalid Email or Mobile No".
10. Stop the program.'''


import re
data=input("Enter email or mobile no: ")
email_pattern= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z09.-]+\.[a-zA-Z]{2,}$'
mobile_pattern=r'[0-9]{10}$'

if re.fullmatch(email_pattern,data):
    print("Valid Email ID")

elif re.fullmatch(mobile_pattern,data):
    print("Valid Mobile No")

else:
    print("Invalid Email or Mobile No")


'''
output:
Enter email or mobile no: abc@gmail.com
Valid Email ID
'''
