str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
str1len = len(str1)
str2len = len(str2)
if str1len == str2len:
    flag = 0
    for i in range (str1len):
        for j in range(str2len):
            if(str1[i] == str2[j]):
                flag = 1
        if (flag == 0):
            break
    if(flag == 1):
        print("Anagrams")
else:
    print("Not anagrams")