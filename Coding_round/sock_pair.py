sock_string = input("Enter the sock string: ")
sock_string = sock_string.upper()
n = len(sock_string)
if n % 2 == 0:
    sorted_string = sorted(sock_string)
    print(sorted_string)
    for i in range(0, n, 2):
        if sorted_string[i] == sorted_string[i+1]:
            continue
        else:
            print("Missing pair of socks")
            break
    print("We have matches for all the socks")
else:
    print("Missing pair of socks")


