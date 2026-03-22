# 1. Get user input and make it an integer.
number = int(input("Enter a number: "))

# 2. Check if remainder when divided by 2 is 0 or not.
if number % 2 == 0:
  print(number, "is an even number")
else:
  print(number, "is an odd number")