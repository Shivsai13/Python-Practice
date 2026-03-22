# Take marks as input from the user
print("Enter Marks Obtained in 4 Subjects: ")
math= int(input("maths: "))
science= int(input("science: "))
english= int(input("english: "))
hindi= int(input("hindi: "))

#Let's calculate the percentage of marks
sum = math + science + english + hindi
print("sum of maths, science, english and hindi is: ", sum)

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)
