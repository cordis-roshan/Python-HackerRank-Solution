if __name__ == '__main__':
    s = input()
    l1 = list(s)
    print(any(x.isalnum() for x in l1))
    print(any(x.isalpha() for x in l1))
    print(any(x.isdigit() for x in l1))
    print(any(x.islower() for x in l1))
    print(any(x.isupper() for x in l1))