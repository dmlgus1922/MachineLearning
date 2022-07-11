n, m = map(int, input('정수 두 개를 입력(구분자 공백): ').split())

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i * j, end = ' ')
    print()
