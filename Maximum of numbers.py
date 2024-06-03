l = []
n = int(input("Enter the upper limit: "))

#Get input numbers and add them to the list
for i in range(0, n):
    a = int(input("Enter a number :"))
    l.append(a)

maxno = l[0]

#Find the maximum number in the list
for i in range(0, len(l)):
    if l[i] > maxno:
        maxno = l[i]

#Print the maximum number
print("The maximum number is %d" % maxno)

