n, s = map(int,input('정수 두 개 입력(구분자: ",")').split(','))
l = list(range(0, n+1,s))
print(*l, sep = ',')
