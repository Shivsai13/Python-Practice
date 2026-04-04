print ("Enter marks obtained in 5 subjects: ")

mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())

tot = mark1 + mark2 + mark3 + mark4 + mark5

avg = tot / 5

print(avg)

if avg >= 91 and avg <= 100:
    print("Your Grade is A1.")

elif avg >= 81 and avg <= 90:
    print("Your Grade is A2.")

elif avg >= 71 and avg <= 80:
    print("Your Grade is B1.")

elif avg >= 61 and avg <= 70:
    print("Your Grade is B2.")

elif avg >= 51 and avg <= 60:
    print("Your Grade is C1.")

elif avg >= 41 and avg <= 50:
    print("Your Grade is C2.")

elif avg >= 33 and avg <= 40:
    print("Your Grade is D.")

elif avg >= 0 and avg <= 32:
    print("Your Grade is E.")

else:
    print("Invalid Input!")