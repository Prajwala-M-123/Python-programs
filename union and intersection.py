#initialize sets
s1 = {10,20,30}
s2 = list(s1)
s3 = {40,50,30}
s4 = list(s3)
s5 = []
#define the union function
def union(s2,s4):
    s5 = list(s2)
    for j in s4:
        if j not in s5:
            s5.append(j)
    return s5
#call the function and store the results
s5 = union(s2,s4)

#print the results
print("s2:",s2)
print("s4:",s4)
print("Union:",s5)

#initialize sets
s1 = {10,20,30,40,60}
s2 = list(s1)
s3 = {40,50,30,40,60}
s4 = list(s3)
s5 = []
#define the union function
def intersection(s2,s4):
    s5 = []
    for i in s2:
        if i in s4:
            s5.append(i)
    return s5
#call the function and store the results
s5 = intersection(s2,s4)

#print the results
print("s2:",s2)
print("s4:",s4)
print("Intersection,:",s5)
