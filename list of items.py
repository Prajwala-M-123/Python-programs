# Initialize a list of items
items = [5,7,10,12,15]
#Print the list of items
print("list of items is",items)
# Prompt the user to enter an item to search  for
x= int(input("enter item to search:"))#11
#Initialize variable for loop control and flagging item  presence
i = flag = 0
#Start a loop to iterate through eeach element of the list
while i < len(items):
    # Check if the current element matches the item being searched for
    if items[i] == x: #11
        #If found, set the flag to indicating presence and exit the loop
        flag = 1
        break
#Move to the next element in the list
    i=i+1

#Check if the flag is set to 1,indicating item presence
if flag == 1:
#If found , print the position (index + 1) of the item in the list
    print("item found at position:", i + 1)
else:
#If not found, print a message indicating absence
    print("item not found")
