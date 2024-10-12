def func(str):
    return str != "s"


l = list(filter(func, "sunday"))
print(l)
