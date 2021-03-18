
while True:
    print("Type the first value you wish to add")
    while True:
        try:
            number1 = int(input("First: "))
            break
        except ValueError:
            print("\nThis is not a number. Try again...")
            print()

    while True:
        try:
            number2 = int(input("Second: "))
            break
        except ValueError:
            print("\nThis is not a number. Try again...")
            print()

    sum = int(number1) + int(number2)
    import sys
    import time

    loading = "\tLOADING"
    bar = " [==========]"
    print(loading)
    for c in bar:
        time.sleep(0.1)
        sys.stdout.write(c)
        sys.stdout.flush()
    print(" ")
    if (sum == 69):
        print("Sum: 69")
        print("hehe the funny number")
    if sum > 1000:
        print("Sum:" + str(sum))
        print("WOW that's a big number")
    if sum < 0:
        print("Sum:" + str(sum))
        print("I didn't even know there was numbers below 0")
    if (0 <= sum < 69) or (69 < sum <= 1000):
        print("Sum:" + str(sum))
        print("What a boring number.")
        print("try something else")
    while True:
        answer = input("Run again? (y/n): ")
        if answer in ("y", "n"):
            break
        print("Invalid input.")
    if answer == "y":
        continue
    else:
        print("Goodbye")
        break