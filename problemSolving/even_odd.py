numList = map(int, input().split())
odd = 0
even = 0
for i in numList:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'홀수 : {odd}', f'짝수 : {even}', sep = '\n')
