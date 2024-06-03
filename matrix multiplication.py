X = [[12,7,3],
     [4,5,6],
     [7,8,9]]
Y = [[5,8,1,2],
     [6,7,3,0],
     [4,5,9,1]]
# Result matrix initialization
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
#Matrix multiplication
for i in range(len(X)):
    for j in range(len(Y[0])):
         for k in range(len(Y)):
             result[i][j]+= X[i][k] * Y[k][j]

#Displaying the result
for r in result:
    print(r)
