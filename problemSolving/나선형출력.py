n = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]
d = x = y = 0

l = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1, n**2 + 1):
    l[y][x] = i
    yy = y+dy[d]
    xx = x+dx[d]
    if 0 <= yy < n and 0 <= xx < n:
        if l[yy][xx] == 0:
            y = yy
            x = xx
        else:
            d = (d+1) % 4
            x += dx[d]
            y += dy[d]
    else:
        d = (d+1) % 4
        x += dx[d]
        y += dy[d]

for i in range(n):
    for j in range(n):
        print(l[i][j], end = '\t')
    print()
