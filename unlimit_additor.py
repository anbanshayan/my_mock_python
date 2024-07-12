user_input = input("Enter numbers = ")

number_list = user_input.split()

sum = 0

for number in number_list:
    number = int(number)
    sum += number
print("Sum of numbers that you have entered so far = ",sum)