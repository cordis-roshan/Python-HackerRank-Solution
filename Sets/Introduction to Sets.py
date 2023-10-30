def average(array):
    arr1 = set(arr)
    average = sum(arr1)/len(arr1)
    return average
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)