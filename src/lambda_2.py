print("Enter the 1st number")
number_1 = int(input(">>> "))
print("Enter the 2nd number")
number_2 = int(input(">>> "))
print("Enter the 3rd number")
number_3 = int(input(">>> "))
lmbd = lambda a, b, c: (a + b + c) / 3
arithmetic = lmbd(number_1, number_2, number_3)
print("Arithmetic mean of 3 nuumber equal " + str(arithmetic))