def second(arg):
    def inner():
        return "outer"+arg()+"outer"
    return inner


def first(arg):
    def inner():
        return " inner "+arg()+" inner "
    return inner


@second
@first
def string():
    return "inside"


print(string())