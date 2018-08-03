# import turtle
# wn = turtle.Screen()
# square = turtle.Turtle()
# f = turtle.Turtle()
#
# def h1():
#     f.forward(30)
#
# def h2():
#     f.left(45)
#
# wn.onkey(h1, "Up")

# square.penup()
# square.right(-180)
# square.forward(90)
# square.left(90)
# square.forward(90)
# square.left(90)
# square.pendown()


# for i in range(4):
#     square.forward(180)
#     square.left(90)
#
# square.penup()
# square.home()
# wn.exitonclick()

# moxie = 'dog'
# anna = 'girl'
# print (moxie < anna and moxie > 'apple' or len(anna) < 3)
# def exor(a, b):
#     y = a and not b or not a and b
#     return y
#
# def mystery(x):
#     a = exor(exor(x,not x),exor(not x,x))
#     return a
#
# n = 47
# result = mystery(n % 47 == 0)
# print(result)

#review starts


# def exor(a, b,c):
#     y = a**b**c
#     return y
#
# def mystery(x):
#     a = exor(x,2,1) + exor(2,1,x)
#     return a
#
# n = 2
# result = mystery(n )
# print(result)

#
# n = 0
# answer = 0
#
# while n < 45:
#     answer = answer + n
#     n = n + 2
# print(answer)

# x = -2
# if x < 0:
#     print(x, "is invalid")
# else :
#     if x > 0:
#         print(x, "is positive")
#     else:
#        print(x, "is 0")

# def remove_vowels(mystring):
#     vowels = "aeiouAEIOU"
#     sWithoutVowels = ""
#     for eachChar in mystring.lower():
#         if eachChar not in vowels:
#             sWithoutVowels = sWithoutVowels + eachChar
#     return sWithoutVowels
#
# print(remove_vowels("maYanja"))

# alist = [['a','b'],'c','d',[['e','f'],'g']]
#
# print(alist[1][0])

#qz 7

# s = "Moxie"
# r = 0
# for item in s:
#     r = r + s.index(item)
# print(r)

# alist = [1, 0, 9, 1]
# blist = alist * 3
# alist[3] = 47
# print(blist)

# alist = [1,0,9,1]
# alist = alist.pop(1)
# print(alist)

# myname = "01001000"
# namelist = myname.split('0')
# init = []
# for aname in namelist:
#     if len(aname)>0:
#         init.append(aname)
# print(init)

# fvar = open('data.csv','r')
# header = fvar.readline()
#
# for v in header.split(','):
#     print (" %s " % v,end='')
# print()
#
# for f in fvar:
#     print (f.split(',')[1:])
#
# fvar.close()

#qz 8
# mydict = {"cat":12, "dog":6, "elephant":23}
# print(mydict["cat"]+mydict["dog"])
#
# mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
# yourdict = mydict
# yourdict["elephant"] = 999
# print(mydict["elephant"])

# i = 0
# n = 10
# while i < n:
#     print(i)
#     i = i + 1

# print(45 + 6 / 3)

# def whole_name(first_name, last_name):
#     return first_name + " " + last_name
#
# print(whole_name("steven","mayanja"))
#
# s = "Python summer"
# for idx in range(1,len(s),2):
#     if idx % 2 == 0:
#         print(s[idx])

# s = "python rocks"
# print(s[1] * s.index("n"))

# def product_two(one, two):
#     return one * two
#
# print(product_two(4,3))

# mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
# yourdict = mydict
# yourdict["elephant"] = 999
# print(mydict["elephant"])



# s = 'moxie, sasha, sandy'
# slist = s.split()
# result = [elt[:-1] for elt in slist]
# print (result)

# n = int(input("Enter N: "))
#
# print("a")
# print("*" * n)
#
# print("\n")
#
#
# print("b")
# for i in range(n):
#     print("*" * n)
#
# print("\n")
#
# print("c")
#
# i = 0
# for i in range(n):
#     print("*" * i)
#     i = i + 1
#
#
# print("d")
# for i in range(n):
#     print("*" * n)
#     n = n -1

# def printPattern(n):
#     k = 0
#     for i in range(1, n + 1):  # row 6
#
#         # Print spaces
#         for j in range(i, n):
#             print(' ', end='')
#
#         # Print #
#         while (k != (2 * i - 1)):
#             if (k == 0 or k == 2 * i - 2):
#                 print('#', end='')
#             else:
#                 print(' ', end='')
#             k = k + 1
#         k = 0;
#         print("")  # print next row
#
#     # print last row
#     for i in range(0, 2 * n - 1):
#         print('#', end='')
#
#
# # Driver code
# n = 6
# printPattern(n)
# size = 5
# inner_size = size - 2
# print ('*' * size)
# for i in range(inner_size):
#     print ('*' + ' ' * inner_size + '*')
# print ('*' * size)
n=4
x = ["*","_"]
for i in range(n):
    for j in range(n):
        print(x[i][j], end=" ")
    print()
