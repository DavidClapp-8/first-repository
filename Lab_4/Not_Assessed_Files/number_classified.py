num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
    if num % 4 == 0:
        print("And it's also divisible by 4")
    if num % 10 == 0:
        print("Is divisable by 10")
    if num % 5 == 0:
        print("Is divisable by 5")
    else:
        print(num, "is odd")