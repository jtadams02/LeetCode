if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    first = -101
    second = 0 
    
    for x in arr:
        if x > first:
            second = first
            first = x
        elif x < first and x > second:
            second = x
    
    print(second)
