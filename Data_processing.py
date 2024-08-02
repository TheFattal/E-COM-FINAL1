# 1:
count: int = 0
sum_input: int = 0
while True:
    try:
        number: int = int(input("Please enter an integer please:"))
        if number != -99:
            count += 1
            sum_input += number
        elif number == -99 and count == 0:
            print("None")
            break
        else:
            print(f"\nThe sum is: {sum_input}")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# 2:
lowest_input = None
highest_input = None
count = 0

while True:
    try:
        number: int = int(input("Please enter an integer please:"))
        if lowest_input is None and number > 0:
            highest_input = number
            lowest_input = number
        elif count == 0 and number == -99:
            print("None")
            break

        if highest_input < number > 0:
            highest_input = number
            count += 1
        elif lowest_input > number > 0:
            lowest_input = number
            count += 1
        elif number <= 0:
            print(f"The highest number is: {highest_input}\nThe lowest number is: {lowest_input}")
            break

    except ValueError:
        print("Invalid input. Please enter a valid integer:")

# 3:
max_int = None
max_index: int = 0
for i in range(5):
    try:
        num_input: int = int(input("Please enter an integer sir:"))
        if max_int is not None and num_input > max_int:
            max_int = num_input
            max_index = i
        elif max_int is None:
            max_int = num_input
            max_index = 0
    except ValueError:
        print("Invalid input. Please enter a valid integer value.")

print(f"\nThe index of the max value inserted is: {max_index}")

# 4:

try:
    num_input1: int = int(input("Please enter an integer sir:"))
    num_input2: int = int(input("Now insert another one:"))
    mul_inputs: int = 0

    for _ in range(num_input2):
        mul_inputs += num_input1
    print(f"\n{num_input1} times {num_input2} is: {mul_inputs}")

except ValueError:
    print("Invalid input. Please enter a valid integer value.")

# 5:
try:
    num_input1: int = int(input("Please enter an integer sir:"))
    num_input2: int = int(input("Now insert another one:"))
    pow_inputs: int = 1

    for _ in range(num_input2):
        pow_inputs = pow_inputs * num_input1
    print(f"\n{num_input1} to the power of {num_input2} is: {pow_inputs}")

except ValueError:
    print("Invalid input. Please enter a valid integer value.")

# 6:

# 7:
num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))

divisors_num1 = []
for i in range(1, num1 + 1):
    if num1 % i == 0:
        divisors_num1.append(i)

divisors_num2 = []
for i in range(1, num2 + 1):
    if num2 % i == 0:
        divisors_num2.append(i)

common_divisors = []
for d in divisors_num1:
    if d in divisors_num2:
        common_divisors.append(d)

if common_divisors:
    gcd = max(common_divisors)
else:
    gcd = 1  # Default to 1 if there are no common divisors

print(f"The greatest common divisor of {num1} and {num2} is: {gcd}")

# 8:
while True:
    try:
        num_input: int = int(input("Please enter a positive integer sir:"))
        is_prime: bool = True
        if num_input <= 1:
            print(f"{num_input} is not prime!")
            break

        for i in range(2, num_input):
            if num_input % i == 0:
                print(f"\nThe {num_input} number is not prime!")
                is_prime = False
                break
                
        if not is_prime:
            break
            
        if is_prime:
            print(f"\n{num_input} is indeed a prime number!")
            break

    except ValueError:
        print("Invalid input. Please enter a valid integer value.")
