def upper_lower(st):
    string_l = []
    for s in st:
        if s == ' ':
            string_l.append(s)
        elif s.isalpha():
            if s.isupper():
                string_l.append(s.lower())
            else:
                string_l.append(s.upper())
        else:
            string_l.append('@')
            return string_l

    return string_l


while True:
    st = input('입력: ')
    result = upper_lower(st)
    if '@' in result:
        print('출력:', ''.join(result[:-1]), '\n')
        print('프로그램이 종료됩니다.')
        break
    else:
        print('출력:', ''.join(result))
