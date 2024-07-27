# 1:
num1: float = float(input("Insert a float number please:"))
num2: float = float(input("Now Insert another float number please:"))
if num1 >= num2:
    print(*[num2 for _ in range(3)])
elif num1 <= num2:
    print(*[num1 for _ in range(3)])
else:
    print("You've type it all wrong. Sorry!...")

# 2:
num1: int = int(input("Enter the first integer:"))
num2: int = int(input("Enter the second integer:"))
print(f"The average is: {(num1 + num2) / 2}")

# 3:
num1: int = int(input("Enter the first integer:"))
num2: int = int(input("Enter the second integer:"))
num3: int = int(input("Enter the third integer:"))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest integer is:", largest)

# 4:
movie_len: int = int(input("Insert movie length in minutes:"))
movie_hours: int = movie_len // 60
movie_minutes: int = movie_len % 60
print(f"The movie is {movie_hours} hours and {movie_minutes} minutes.")

# 5:
number: int = int(input("insert a 4 digits integer please:"))
print(f"The rightmost digit is: {number % 10}")

# 6:
number: int = int(input("insert a 4 digits integer please:"))
print(f"The tens digit is: {(number % 100) // 10}")

# 7:
number: int = int(input("insert a 2 digits integer please:"))
if number // 100 == 0:
    print(f"The number's digits sum is: {(number % 100) // 10 + number % 10}")
else:
    print("You've type it wrong sir!")

# 8:
number: int = int(input("insert a 2 digits integer please:"))
if number // 100 == 0:
    print(f"The new swap number is: {number % 10 * 10 + number // 10} ")
else:
    print("You've type it wrong sir!")
# 9:
number: int = int(input("insert an integer number please:"))
if number % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")

# 10:
# Get user input
try:
    salary: float = float(input("Enter your salary in NIS: "))
    if salary < 0:
        print("Salary cannot be negative.")
    else:
        tax: float = 0

        if salary > 50000:
            tax += (salary - 50000) * 0.51
            salary = 50000
        if salary > 35000:
            tax += (salary - 35000) * 0.45
            salary = 35000
        if salary > 25000:
            tax += (salary - 25000) * 0.40
            salary = 25000
        if salary > 18000:
            tax += (salary - 18000) * 0.30
            salary = 18000
        if salary > 12000:
            tax += (salary - 12000) * 0.20
            salary = 12000
        if salary > 6000:
            tax += (salary - 6000) * 0.10

        # Print the total tax
        print(f"The total tax to pay is: NIS {tax:.2f}")

except ValueError:
    print("Invalid input. Please enter a numeric value for the salary.")

# 11:
age: int = int(input("Please insert your age:"))
height: int = int(input("Please insert your height:"))
if (height > 115 and age >= 8) or (height > 100 and age > 18):
    print("You are allowed to enter!")
else:
    print("You're not allowed to enter!")
