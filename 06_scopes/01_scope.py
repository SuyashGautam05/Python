username = "Hello this is global scope"

def func():
    username = "This is function scope"
    print(username)

print(username)
func()

x = 99

def func2(y):
    z = x + y
    return z
Result = func2(1)
print(Result)

def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult

