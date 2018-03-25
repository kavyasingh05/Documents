def remove_duplicate(a):
    newab = []
    for x in range(len(a)):
        if a[x] not in newab:
            newab.append(a[x])
        print(newab)

    return newab
