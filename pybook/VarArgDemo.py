def printMax(x = 11, *numbers, y = 23):
    print(y)
    if len(numbers) == 0:
        print("No arguments passed")
    else:
        max = numbers[0]
        for item in numbers[1 : ]:
            if max < item:
                max = item

        print("The maximum value is", min(numbers))

printMax(x = 12, numbers = 3, 4, y = 34)
#printMax(5)
#printMax(1, 2, 4, 5, 1)
#printMax(10, 1, -5, -2, -4, 15, 12)