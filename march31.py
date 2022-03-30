'''
# 2차원 리스트
a = [[10, 20], [30, 40], [50, 60]]
print(a[0][0])

a = [[10, 20], [30, 40], [50, 60]]
# for문
for i in range(len(a)):            # 세로 크기
    for j in range(len(a[i])):     # 가로 크기
        print(a[i][j], end=' ')
    print()

a = [[10, 20], [30, 40], [50, 60]]
 # while문
i = 0
while i < len(a):    # 반복할 때 리스트의 크기 활용(세로 크기)
    x, y = a[i]      # 요소 두 개를 한꺼번에 가져오기
    print(x, y)
    i += 1           # 인덱스를 1 증가시킴

# for반복문으로 리스트 만들기

a = []
for i in range(10):
    a.append(0)
'
a = []
for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)

print(a)

# 3차원 리스트
# [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
# col = 열, row = 행, dpeth = 층

a = [[[0 for col in range(3)]for row in range(4)]for depth in range(2)]
print(a)
'''
# 23.7 지뢰찾기********************
col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(col):
    for j in range(row):
        if matrix[i][j] == "*":
            print("*",end="")

        else:
            cnt = 0
            for ii in range(i - 1, i + 2):
                for jj in range(j - 1, j + 2):
                    if ii<0 or jj<0 or ii>=row or jj>=col:
                        continue
                    elif matrix[ii][jj] == "*":
                        cnt += 1
            print(cnt, end='')
    print()

