# username = "Ali Akbar"


# def test():
#     # username = "Ali"
#     print(username)


# print(username)
# print(test())

x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(2)

# print(result)


# def func3():
#     global x
#     x = 88


# func3()
# print(x)


def f1():
    x = 88

    def f2():
        print(x)

    return f2


myresult = f1()
myresult()


def coder(num):
    def actual(x):
        return x**num

    return actual


f = coder(2)
g = coder(3)

print(f(3))
print(g(3))
