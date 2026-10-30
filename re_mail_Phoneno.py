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
