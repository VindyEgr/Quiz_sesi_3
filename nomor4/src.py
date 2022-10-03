A = [[5,3],
     [3,4]]

B = [[6,3],
     [7,3]]

hasil = [[0,0],
         [0,0]]

for i in range (len(A)):
  for j in range (len(A[0])):
    hasil [i][j] = A[i][j] - B[i][j]

for x in hasil:
  print(x)