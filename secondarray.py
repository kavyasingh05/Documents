def my_sort(a):
    for y in range(0,len(a)):
        for x in range(y+1,len(a)):
            if a[y] > a[x]:
                temp = a[y]
                a[y] = a[x]
                a[x] = temp
    return a

    
        
