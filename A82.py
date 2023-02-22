def dups():
    collection = [99,86,87,88,111,86,103,87,94,78,77,85,86,120]

    duplicate=[]
    for i in collection:
        if i in duplicate:
            continue
        elif collection.count(i)>1:
            duplicate.append(i)
    print(duplicate)

dups()