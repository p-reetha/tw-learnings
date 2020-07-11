g = lambda x: round(x ** (1./3))

cubic_number = int(input("Enter a number: "))
num = g(cubic_number)
if num**3 == cubic_number:
    print("True")
else:
    print("False")
