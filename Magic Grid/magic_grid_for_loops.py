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
s=sum(matrix[0])
for i in range(len(matrix)):
    total_sum=0
    for j in range(len(matrix[0])):
        total_sum=total_sum+matrix[i][j]
    if(s!=total_sum):
        flag=0
        break
for i in range(len(matrix[0])):
    total_sum=0
    for j in range(len(matrix)):
        total_sum=total_sum+matrix[i][j]
    if(s!=total_sum):
        flag=0
        break
total_sum=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if (i==j):
            total_sum=total_sum+matrix[i][j]
if(s!=total_sum):
    flag=0
if flag==1:
    print('Magic Square')
else:
    print('Not Magic Square')
