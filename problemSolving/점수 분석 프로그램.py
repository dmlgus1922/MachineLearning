def program(n, students, scores):
    if n == 1:
        students = int(input('학생수> '))
        scores = list(range(students))
        return students, scores

    elif n == 2:
        for i in range(students):
            scores[i] = int(input(f'scores[{i}]> '))
        return students, scores

    elif n == 3:
        for i in range(students):
            print(f'scores[{i}]: {scores[i]}')
        return students, scores

    elif n == 4:
        avg = sum(scores) / students
        print(f'최고 점수: {max(scores)}')
        print(f'평균 점수: {avg}')
        return students, scores

    elif n == 5:
        print('프로그램 종료')
        return 0, 0

students = 0
scores = []
while True:
    n = int(input('선택> '))
    students, scores = program(n, students, scores)
    if n == 5:
        break
