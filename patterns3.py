_author_ = "Stephen Mayanja"

n = int(input("Enter N: "))


def diamondShape(n):
    for x in range(n - 1):
        print((n - x) * ' ' + (2 * x + 1) * '*')
    for x in range(n - 1, -1, -1):
        print((n - x) * ' ' + (2 * x + 1) * '*')

        #Method below does the same thing

    # for x in list(range(n)) + list(reversed(range(n - 1))):
    #     print('{: <{w1}}{:*<{w2}}'.format('', '', w1=n - x - 1, w2=x * 2 + 1))

def diamondWithSpace(n):
      for x in list(range(n)) + list(reversed(range(n - 1))):
          print('{: <{w1}}{:*<{w2}}'.format('', '', w1=n - x - 1, w2=x * 2 + 1))


def triangleShape(n):
    for number in range(0, n):
        print (" " * number + "*" * (n - number))

def squareShape(n):
        for i in range(n):
            for j in range(n):
                print('*' if i in [0, n - 1] or j in [0, n - 1] else ' ', end='')
            print()


print("part A: triangle shape:")
triangleShape(n)
print("part B: Square shape with spaces:")
squareShape(n)
print("part C: diamond shape:")
diamondShape(n)
print("part D: diamond shape with spaces in between:")
diamondWithSpace(n)