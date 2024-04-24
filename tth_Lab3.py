import math

cResult = 0.0
sum = 0
calcs = 0
average = 0

print(f"Current Result: {cResult}\n")

while True:
    print("Calculator Menu\n"
          "---------------\n"
          "0. Exit Program\n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. Exponentiation\n"
          "6. Logarithm\n"
          "7. Display Average\n")

    while True:
        number = input("Enter Menu Selection: ")

        if number > "7" or number < "0":
            print("\nError: Invalid selection!")
        else:
            if number == "7":
                if calcs == "0":
                    print("Error: No calculations yet to average!\n")
                else:
                    average = sum/calcs
                    print(f"\nSum of calculations: {round(sum, 2)}\n"
                          f"Number of calculations: {calcs}\n"
                          f"Average of calculations: {round(average, 2)}\n")
            else:
                break

    if number == "0":
        print("\nThanks for using this calculator. Goodbye!")
        break
    else:
        num1 = float(input("\nEnter first operand: "))
        num2 = float(input("Enter second operand: "))

        match number:
            case "1":
                cResult = num1 + num2
            case "2":
                cResult = num1 - num2
            case "3":
                cResult = num1*num2
            case "4":
                cResult = num1/num2
            case "5":
                cResult = num1**num2
            case "6":
                cResult = math.log(num2, num1)

        calcs += 1
        sum += cResult

        print(f"\nCurrent Result: {round(cResult, 2)}\n")