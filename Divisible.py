print ("Enter a number (Numerator): ")
numn = int(input())
print ("Enter a number (Denominator): ")
numd = int(input())

if (numn % numd == 0):
    print (str(numn) + " is divisible by " + str(numd))
else:
    print (str(numn) + " is not divisible by " + str(numd))