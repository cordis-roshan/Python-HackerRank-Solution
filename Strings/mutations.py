def mutate_string(string, position, character):
    l = list(string)
    position = int(position)
    l[position] = character
    o = ''.join(l)
    return o

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, i, c)
    print(s_new)