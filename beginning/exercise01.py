# exercise1
def ex1():
    a = int(input())
    b = int(input())
    z = a * b
    if z <= 1000:
        print(z)
    else:
        print(a + b)


# ex1()

# exercise2
def ex2():
    for i in range(11):
        if i == 0:
            print("current number ", 0, " previous number", 0, "sum ", 0)
        else:
            print("current number ", i, " previous number", i - 1, "sum ", i + i - 1)


# ex2()

# exercise3
def ex3():
    word = input()
    print("Original word is", word)
    z = list(word)
    print(z)
    for i in range(len(z)):
        if i % 2:
            print(z[i])
    # l = [i for i in range(len(z)) if i%2]
    # print(l)
    l = [j for i, j in enumerate(z) if i % 2]
    print(l)


# ex3()

# exercise4
def removech(word, n):
    myl = list(word)
    newword = []
    for i in range(n, len(myl)):
        newword.append(myl[i])
    return "".join(newword)

def ex4():
    word = input()
    print("original word is ", word)
    print("how much letters to be removed?")
    n = int(input())

    print(removech(word, n))


#ex4()


#exercise5

a = [556, 554, 66, 556]
b = [559, 55, 66, 556]

def are_first_and_last_equal(a):
    if len(a) <= 0:
        print ("no elements")
        return
    if a[0] == a[-1]:
        print("first and last are equal")
    else:
        print("first and last are no equal")


#are_first_and_last_equal([8])

#exercise6
def ex6():
    a = [12, 30, 54, 72, 65, 80]
    devisibleby5 = [i for i in a if i % 5 == 0]
    print(devisibleby5)

#ex6()
#alternative
#y = list(filter(lambda x: x % 5 == 0, [12, 30, 54, 72, 65, 80]))
#print(y)

#exercise7
def ex7():
    str = "Radica tries to learn Python. Martin helps Radica a lot.".lower()
    x = str.count("radica".lower())
    print(x)
#lower is method for string
#ex7()


#exercise8
def ex8():
    n = int(input())
    for i in range(1, n+1):
        print(" ".join(str(i) * i), end="")
        # print(" ".join([str(i) for _ in range(i)]), end="")
        # for j in range(i):
        #     print(i, "", end="")
        print()
#ex8()


#exercise9
def ex9():
    print("enter a number")
    n = int(input())
    def isPalindrom(n):
        x = list(str(n))
        y = [i for i in x]
        y.reverse()
        if x == y:
            return True
        else:
            return False

    print("the following number is {0}a palindrom".format("" if isPalindrom(n) else "not "))
#ex9()


#exercise10
def ex10():
    a = [35, 43, 54, 51, 18, 20, 39]
    b = [4, 5, 6, 7]

    def new_array(a, b):
        # c = [a[i] for i in range(a) if not a[i] % 2]
        # d = [b[i] for i in range(b) if b[i] % 2]
        # c.extend(d)
        # return c
        return list(filter(lambda x: x % 2, a)) + list(filter(lambda x: not x % 2, b))

    print(new_array(a, b))
#ex10()


#exercise11
def ex11():
    n = input()
    y = list(n)
    y.reverse()
    print(" ".join(y))
#ex11()

#exercise12

def ex12():
    print("Enter the income")
    income = int(input())
    def tax(income):
        if income <= 10000:
            tax = 0
        elif 10000 < income <= 20000:
            tax = ((income/100)*10)
        else:
            tax = ((10000/100)*0)+((10000/100)*10)+(((income-10000-10000)/100)*20)
        return tax
    print("The tax for this income is",tax(income))

#ex12()

#exercise13

def ex13():
    for i in range (1, 11):
        for x in range(1, 11):
            print(("  "+str(x*i) if x*i < 10 else (" "+str(x*i) if x*i < 100 else(x*i))), end=" ")
            #print(("  " if x*i < 10 else (" " if x*i < 100 else ""))+str(x*i), end=" ")
        print()

#ex13()


#exerice14
def ex14():
    for i in range(5, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
#ex14()

#exercise15

base = int(input())
exp = int(input())
def exponent(base, exp):
    if base < 0 or exp < 0:
        raise Exception("enter positive integers for base and exp")
    return(base**exp)
# print(exponent(base,exp))
# if there is an issue I want x to be set to some default value 42.
try:
    x = exponent(base, exp)
except:
    print("there is an issue with the passed arguments")
    x = -1
print(x)