f= open("preetha.txt","w+")
f.write("A.Preetha\n")
f.write("24.08.1999\n")
f.close()
f=open("preetha.txt", "a+")
f.write("B.E")
f.close()
f=open("preetha.txt", "r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)

'''
f1 = f.readlines()
for x in f1:
    print(x)
'''