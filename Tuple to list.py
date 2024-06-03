#initalizing empty tuples
tuple1 =()
tuple2 =()
#converting empty tuples to empty lists
l1 = list(tuple1)
l2 = list(tuple2)

#prompting user to enter the total count of elements
count = int(input("Enter the total count of elements: "))
#adding elements to tuple1
print("Enter elements for tuple1: ")
for i in range(0, count):
    l1.append(str(input()))
#adding elements to tuple2
print("Enter elements for tuple2: ")
for i in range(0, count):
    l2.append(str(input()))
#converting lists back to tuples
tuple1 = tuple(l1)
tuple2 = tuple(l2)
#printing tuple1 and tuple2
print("Tuple1: ",tuple1)
print("Tuple2: ",tuple2)
#creating a new tuple containing the maximum elements from tuple1 and tuple2
tuple3 = (max(tuple1), max(tuple2))
#printing the maximum of tuple1 and tuple2
print("Max of tuple1 & tuple2 :",tuple3)
