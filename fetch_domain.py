import re
url = re.search(r'(https?://)?(www\.)?(\w+)(\.\w+)',input("Enter an URL: "))
if url:
    domain = url.group(3,4)
    print("".join(domain))
else:
    print("Not an URL")