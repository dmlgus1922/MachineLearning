import pickle

notion = '''----------------------------------------------------------------
1.계좌생성 | 2.계좌목록 | 3.예금 | 4.출금 | 5.송금 | 6.고객삭제 | 7.종료
----------------------------------------------------------------
'''
try:
    accounts = pickle.load(open('account_list.p', 'rb'))
except:
    accounts = []

def account(n):
    global accounts
    if n == 1:
        info = {}
        print('''-------------- 
계좌생성
--------------''')
        number = input('계좌번호: ')
        name = input('계좌주: ')
        money = int(input('초기입금액: '))
        info['number'] = number
        info['name'] = name
        info['money'] = money
        accounts.append(info)
        input('결과: 계좌가 생성되었습니다.')

    if n == 2:
        print('''-------------- 
계좌목록
--------------''')
        if not accounts:
            input('계좌목록이 비어 있습니다.')
            return
        else:
            for ac in accounts:
                for value in ac.values():
                    print(value, end = '\t')
                print()
            input('계좌목록이 출력되었습니다.')

    if n == 3:
        print('''-------------- 
예금
--------------''')
        number = input('계좌번호: ')
        for ac in accounts:
            if ac['number'] == number:
                break
        else:
            input('등록된 계좌가 없습니다.')
            return
        money = int(input('예금액: '))
        ac['money'] += money
        input('예금이 성공되었습니다.')

    if n == 4:
        print('''-------------- 
출금
--------------''')
        number = input('계좌번호: ')
        for ac in accounts:
            if ac['number'] == number:
                break
        else:
            input('등록된 계좌가 없습니다.')
            return

        try:
            money = int(input('출금액: '))
            if ac['money'] < money:
                raise Exception('잔액이 부족합니다.')
            ac['money'] -= money
            input('출금이 성공되었습니다.')
        except Exception as e:
            input(e)

    if n == 5:
        print('''-------------- 
송금
--------------''')
        out_number = input('출금할 계좌: ')
        for ac in accounts:
            if ac['number'] == out_number:
                break
        else:
            input('등록된 계좌가 없습니다.')
            return
        out_ac = ac

        in_number = input('송금할 계좌: ')
        for ac in accounts:
            if ac['number'] == in_number:
                break
        else:
            input('등록된 계좌가 없습니다.')
            return
        in_ac = ac

        try:
            money = int(input('송금액: '))
            if out_ac['money'] < money:
                raise Exception('잔액이 부족합니다.')
            out_ac['money'] -= money
            in_ac['money'] += money
            input('송금이 성공되었습니다.')
        except Exception as e:
            input(e)

    if n == 6:
        number = input('삭제할 고객의 계좌를 입력하세요. ')
        for ac in accounts:
            if ac['number'] == number:
                break
        else:
            input('등록된 계좌가 없습니다.')
            return
        accounts.pop(accounts.index(ac))
        input('고객 삭제를 완료했습니다. ')

while True:
    print(notion)
    n = int(input('선택> '))
    if n == 7:
        print('프로그램 종료')
        break
    account(n)

pickle.dump(accounts, open('account_list.p', 'wb'))