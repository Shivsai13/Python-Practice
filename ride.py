print("Select your ride: ")
print("1. Bike")
print("2. Car")

# Take input of number 1 or 2
choice = int(input("Enter your choice: "))

# User entering option 1
if choice == 1: 
    print("\nWhat type of bike?")
    print("1. Scooty")
    print("2. Scooter")
    
    choice2 = int(input("Enter your choice: "))
    
    if choice2 == 1:
        print("You have selected Scooty.")
    else:
        print("You have selected Scooter.")

# User entering option 2
elif choice == 2:
    print("\nWhat type of car?")
    print("1. Sedan")
    print("2. XUV")
    
    choice3 = int(input("Enter your choice: "))
    
    if choice3 == 1:
        print("You have selected Sedan.")
    else:
        print("You have selected XUV.")

# Outer else statement for invalid main choice
else:
    print("Wrong choice!")