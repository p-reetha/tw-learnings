import re
if re.match(r'^[-+]?[0-9]*\.[0-9]+$',input("Enter a number to check: ")):
    print("Float")
else:
    print("Not float")