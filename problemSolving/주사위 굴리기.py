import random
n = int(input('게임횟수를 입력하시오: '))
print(f'게임을 {n}회 시작합니다.')

win = 0
lose = 0
draw = 0
results = ['결과', f'{n}번 경기내용']

for i in range(1, n+1):
    com_num = random.randint(1,6)
    print(f'{i}회차', f'컴퓨터: {com_num}', sep = '\n')
    input('주사위를 굴리시오')
    player_num = random.randint(1,6)
    print(f'플래이어 {player_num}','\n')
    if player_num > com_num:
        win += 1
        result = f'{i}회차 - 플래이어: {player_num}, 컴퓨터: {com_num} 승리'
        results.append(result)
    elif player_num < com_num:
        lose += 1
        result = f'{i}회차 - 플래이어: {player_num}, 컴퓨터: {com_num} 패배'
        results.append(result)
    else:
        draw += 1
        result = f'{i}회차 - 플래이어: {player_num}, 컴퓨터: {com_num} 비김'
        results.append(result)

print(*results, sep = '\n')
print(f'게임수: {n}회 승리: {win}회 비김: {draw}회 패배: {lose}회')