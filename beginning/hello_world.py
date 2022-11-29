print("hello world")
a = 10

def foo(x):
    return "{1}hello {0} ".format(x, "*")

def join(y):
    z = ""
    for i in y:
        z = z+i
    return z

foo("asia")

# b = []
# for _ in range(4):
#     b.append(input())
# print(b)
x = ["mace", "radi", "hoho", "fefe"]
foo(x)
z = list(map(foo, x))
print(z)
print(join(z))

