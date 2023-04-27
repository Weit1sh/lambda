print("Enter the side of square")
side = int(input(">>> "))
lmbd = lambda a: a * a
perimeter = lmbd(side)
print("Perimeter the square with " + str(side) + " is equal to " + str(perimeter))