def function_outside():
    msg = "Hi"

    def function_inside():
        msg = "Hello"
        print(msg)
        return msg
    s = function_inside()
    print(s)


function_outside()

