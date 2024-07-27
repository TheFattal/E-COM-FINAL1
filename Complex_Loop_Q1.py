# 1:
import math
temp_list = [float('nan') for _ in range(12)]
while True:
    while any(math.isnan(item) for item in temp_list):
        try:
            for i in range(12):
                user_input: float = float(input("Enter a ticket temperature please:"))
                temp_list[i] = user_input
        except ValueError:
            print("Invalid input. Please enter a valid float value.")
    if all(5.0 < value < 40.0 for value in temp_list):
        print(f"\nThe temperatures are:\n{temp_list}\nAll data is correct!\n")
        print(f"The average is: {sum(temp_list) / len(temp_list):,.2f}")
        print(f"The highest temperature is: {max(temp_list):,.2f}")
        print(f"The lowest temperature is: {min(temp_list):,.2f}")
        break
    elif any(temp_list[i] == 0.0 and temp_list[i + 1] == 0.0 for i in range(len(temp_list) - 1)):
        print("Wrong data! 2 zeroes - Type it all again!")
        temp_list = [float('nan') for _ in range(12)]
        continue
    else:
        print(f"\nThe temperatures are:\n{temp_list}\nWrong data! Bye Bye!")
        break
