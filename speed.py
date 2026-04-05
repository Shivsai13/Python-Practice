a = int(input("Enter a value:"))
b = int(input("Enter value 2:"))
c = int(input("Enter value 3:"))

avg = (a + b + c) / 3
print ("avg=", avg)

if avg > a and avg > b and avg > c:
    print("%d is greater than %d, %d and %d" % (avg, a, b, c))
elif avg > a and avg > b:
    print("%d is greater than %d and %d" % (avg, a, b))
elif avg > a and avg > c:
    print("%d is greater than %d and %d" % (avg, a, c))
elif avg > b and avg > c:
    print("%d is greater than %d and %d" % (avg, b, c))
elif avg > a:
    print("%d is greater than %d" % (avg, a))
elif avg > b:
    print("%d is greater than %d" % (avg, b))
elif avg > c:
    print("%d is greater than %d" % (avg, c))
else:
    print("%d is not greater than %d, %d and %d" % (avg, a, b, c))