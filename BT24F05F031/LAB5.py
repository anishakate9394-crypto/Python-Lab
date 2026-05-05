num = int(input("Enter number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif num == 0:
    print("Zero")
else:
    print("Negative")