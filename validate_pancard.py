import re
if re.match(r'^[A-Z]{5}\d{4}[A-Z]$',input("Enter a PAN number to check: ")):
    print("Valid")
else:
    print("Invalid")