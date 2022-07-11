n = int(input('정수 1개를 입력: '))

for i in range(1, 101):
    if i < n:
        print(i, end = ',')
    else:
        print('사용자의 요청에 의해 종료')
else:
    print('\b')
