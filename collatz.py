def collatz():

    try:
        num = int(input("Enter a number:\n"))
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                print(num)
            else:
                num = (num * 3) + 1
                print(num)
    except ValueError:
        print("You must enter an integer!")
        collatz()


collatz()
