sock_string = input("Enter the sock string: ")
sock_string = sock_string.upper()
n = len(sock_string)
if n % 2 == 0:
    sorted_string = sorted(sock_string)
    print(sorted_string)
    for i in range(0, n, 2):
        if sock_string[i] == sorted_string[i+1]:
            print("We have matches for all the socks")
        else:
            print("Missing pair of socks")
            break
else:
    print("Missing pair of socks")


