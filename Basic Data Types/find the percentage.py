if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    op = list(student_marks[query_name])
    per = sum(op)/len(op)
    print(f"{per:.2f}")