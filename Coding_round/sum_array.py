array = [1, 1, 1, 1]
n = len(array)
count = 0
sum = 2
for i in range(0, n):
    for j in range(i+1, n):
        a = array[i]
        b = array[j]
        if a + b == sum:
            count += 1
            # print("Pair {} {}".format(array[i], array[j]))
        else:
            continue
print(count)