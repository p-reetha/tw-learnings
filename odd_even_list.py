lis = []
for num in range(int(input("Enter the limit: "))):
    if num%2 == 0:
        lis.append('Even')
    else:
        lis.append('Odd')
print(lis)