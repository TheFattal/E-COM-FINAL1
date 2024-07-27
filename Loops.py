# 1:
number = None
while number is None:
    try:
        input_value: int = int(input("Enter a positive integer: "))
        if input_value <= 0:
            print("Please enter a positive integer greater than zero.")
        elif isinstance(input_value, int):
            # If valid - set the number and break out of the loop
            number = input_value
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

numbers = [str(i) for i in range(1, number + 1)]
print(' '.join(numbers))

# 2:
number1 = None
number2 = None
while number1 is None:
    try:
        input_value1: int = int(input("Enter an integer: "))
        input_value2: int = int(input("Enter another integer: "))
        if isinstance(input_value1, int) and isinstance(input_value2, int):
            number1 = input_value1
            number2 = input_value2
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if number1 > number2:
    numbers = [str(i) for i in range(number2, number1 + 1)]
    print(' '.join(numbers))
elif number2 > number1:
    numbers = [str(i) for i in range(number1, number2 + 1)]
    print(' '.join(numbers))
# EQUAL case:
else:
    print(f"{number1}")

# 3:
try:
    number: int = int(input("Enter a positive integer: "))
    if number <= 0:
        print("Please enter a positive integer greater than zero.")
    else:
        even_numbers = [str(i) for i in range(1, number + 1) if i % 2 == 0]
        print(' '.join(even_numbers))

except ValueError:
    print("Invalid input. Please enter a valid integer.")

# 4:
try:
    den1 = int(input("Enter the den please: "))
    max1 = int(input("Enter the max please: "))
    if number <= 0 or den1 <= 0:
        print("Please enter a positive integer greater than zero.")
    elif number1 > 0 and number2 > 0:
        den_numbers = [str(i) for i in range(1, max1 + 1) if i % den1 == 0]
        print(' '.join(den_numbers))

except ValueError:
    print("Invalid input. Please enter a valid integer.")