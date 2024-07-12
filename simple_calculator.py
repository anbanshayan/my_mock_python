#my own calculator

Addition = '+',
Subtraction = '-',
Multiplication = '*',
Division = '-'

operand_input = input("Enter Your Operand + - * / => ")
num1 = int(input("Enter number = "))
num2 = int(input("Enter number = "))

if operand_input == '+':
    print("Sum = ",num1+num2)
elif operand_input == '-':
    print("Sum = ",num1-num2)
elif operand_input == '*':
    print("Sum = ",num1*num2)
else:
    if num1 or num2 == 0:
        print("Error cannot divide by zero")
    else:
        print("Value = ",num1/num2)
print()
print("Evalute Over!!")