if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    # The default / operator uses float division
    # We usually will want the floor division when it comes to Python
    # which is the // operator
    
    print(a//b)
    print(a/b)