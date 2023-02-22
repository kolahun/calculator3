def unique():
    collection = [99,86,87,88,111,86,103,87,94,78,77,85,86,120]
    n=len(collection)
    a=[]
    for i in collection: 
        for s in range(0,n):
            if collection[s] not in a:
                a.append(collection[s])
                s+=1
    print(a)
unique()