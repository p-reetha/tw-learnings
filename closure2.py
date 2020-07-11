def f(x):
    def g(y):
        return y
    return g(x)


a = 5
b = 1
h = f(b)
print(h)

