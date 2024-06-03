#initialize dictionary with operators as keys and lists of numbers as values
dict1 = {
    "+":[100,200],
    "-":[50,40],
    "*":[30,78],
    "/":[10,2]
}
#prompt user to enter an operator
x = input("Enter an operator: ")
print("Operator entered: ",x)
#define the add function
def add():
    a = dict1["+"]
    print("Numbers to add: ",a)
    b = a[0] + a[1]
    print("Results of addition: ",b)
#define the subtract function
def sub():
    a = dict1["-"]
    print("Numbers to sub: ",a)
    b = a[0] - a[1]
    print("Results of subtraction: ",b)
#define the multiplication function
def mul():
    a = dict1["*"]
    print("Numbers to multiply: ",a)
    b = a[0] * a[1]
    print("Results of multiplication: ",b)
#define the divide function
def div():
    a = dict1["/"]
    print("Numbers to divide: ",a)
    b = a[0] / a[1]
    print("Results of division: ",b)
#Execute the corresponding function based on the operator entered by the user
if x == "+":
    add()
elif x == "-":
    sub()
elif x == "*":
    mul()
elif x == "/":
    div()
else:
    print("invalid operator")

