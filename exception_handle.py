while 1==1:
    try:
        number = int(input("Enter an integer: "))
        print("Entered an integer")
        break
    except:
        print("Oops! That was not an integer")
        continue
