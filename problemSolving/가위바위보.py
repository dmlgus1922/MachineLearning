import random
print('가위,바위,보 게임을 시작합니다.')
rsp = ['가위','바위','보']
win = 0
wins = 0
wins_list = []
game = 0
while True:
    game += 1
    player_rsp = input('입력: ')
    while player_rsp not in rsp:
        player_rsp = input('가위, 바위, 보 중에 하나를 입력하세요.\n입력: ')
    com_rsp_idx = random.randint(0,2)
    com_rsp = rsp[com_rsp_idx]
    if player_rsp == com_rsp:
        wins_list.append(wins)
        wins = 0
        print(f'컴퓨터: {com_rsp} 플래이어: {player_rsp} 비김','\n')

    elif player_rsp == '가위':
        if com_rsp == '보':
            win += 1
            wins += 1
            print(f'컴퓨터: {com_rsp} 플래이어: {player_rsp} 승리','\n')
        elif com_rsp == '바위':
            wins_list.append(wins)
            print(f'컴퓨터: {com_rsp} 플래이어: {player_rsp} 패배')
            print('패배로 인한 게임 종료','\n')
            break
    elif player_rsp == '바위':
        if com_rsp == '가위':
            win += 1
            wins += 1
            print(f'컴퓨터: {com_rsp} 플래이어: {player_rsp} 승리','\n')
        elif com_rsp == '보':
            wins_list.append(wins)
            print(f'컴퓨터: {com_rsp} 플래이어: {player_rsp} 패배')
            print('패배로 인한 게임 종료','\n')
            break
    elif player_rsp == '보':
        if com_rsp == '바위':
            win += 1
            wins += 1
            print(f'컴퓨터: {com_rsp} 플래이어: {player_rsp} 승리','\n')
        elif com_rsp == '가위':
            wins_list.append(wins)
            print(f'컴퓨터: {com_rsp} 플래이어: {player_rsp} 패배')
            print('패배로 인한 게임 종료','\n')
            break

if not wins_list:
    wins = 0
else:
    wins = max(wins_list)
print('결과', f'게임수: {game}회 승리: {win}회 연승: {wins}회', sep = '\n')