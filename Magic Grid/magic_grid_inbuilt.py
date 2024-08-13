matrix=[]
flag=1
while True:
    r=input()
    if r=='':
        break
    matrix.append(list(map(int, r.split())))
'''matrix = [
            [8, 1, 6],
            [3, 5, 7],
            [4, 9, 2]
          ]
'''
n = len(matrix)
s=sum(matrix[0])
for i in range(n):
        if sum(matrix[i])!= s or sum(row[i] for row in matrix) != s:
            flag = 0
            break
if sum(matrix[i][i] for i in range(n)) != s:
        flag = 0
if sum(matrix[i][n-i-1] for i in range(n)) != s:
        flag = 0
if flag==1:
    print('Magic Square')
else:
    print('Not Magic Square')
