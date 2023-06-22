# This challenge demonstrates list comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lists = []
    # Just need a ton of nested loops
    # and for each loop the range must be inclusive, so we will add 1 to each
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if i+j+k != n: 
                    temp_list = [i,j,k]
                    lists.append(temp_list)
    print(lists)
        