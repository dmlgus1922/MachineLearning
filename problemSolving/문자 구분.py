import string
upper = ''
lower = ''
number = ''
korean = ''
else_ = ''

str_ = input('문자열을 입력하세요 : ')
for s in str_:
    if s == ' ':
        continue
    if s in string.ascii_uppercase:
        upper += s
    elif s in string.ascii_lowercase:
        lower += s
    elif s.isdigit():
        number += s
    elif s.isalpha():
        korean += s
    else:
        else_ += s
        
print('대문자: ', upper, '\n', '소문자: ', lower,'\n', '숫자: ', number, '\n', '한글: ', korean, '\n', '기타: ', else_, sep = '')
