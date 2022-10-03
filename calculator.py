#Python Program to make simple calculator

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    option = input("Enter a Option: ")

    if option in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if option == '1':
            total = num1 + num2
            print("Addition of ", num1, " and ", num2, " is ", total)
        elif option == '2':
            total = num1 - num2
            print("Subtraction of ", num1, " and ", num2, " is ", total)
        elif option == '3':
            total = num1 * num2
            print("Multiplication of ", num1, " and ", num2, " is ", total)
        elif option == '4':
            total = num1 / num2
            print("Division of ", num1, " and ", num2, " is ", total)
    elif option == '5':
        break
    else:
        print("Invalid Option!")
