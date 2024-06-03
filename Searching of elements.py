#creating an empty list
list1 = []
#number of elements as input
n= int(input("Enter number of elements : "))
#iterating till the range
for i in range(0,n):
    ele = int(input())
    list1.append(ele) # adding the element
print("List after initial elements: ", list1)
#prompt for additional elements
m = int(input("Enter number of additional elements : "))
#adding additional elements to the list
for i in range(0,m):
    ele1 = int(input())
    list1.append(ele1) #adding the element
print("List after adding additional  elements : ", list1)
#prompt for index to be printed
p = int(input("Enter the index from the list to be printed: "))
try:
    index = list1.index(p)
    print("The element at index", index, "in the list is:",p)
except ValueError:
    print("Element",p, "not found in the list.")
    
