import re
T = int(input())
for i in range(T):
    value = input()
    try:
        re.compile(value)
        print(True)
    except re.error:
        print(False)
