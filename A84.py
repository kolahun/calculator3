def cumulative_product():
    collection = [1,2,3,4,5,6,7,8]
    a=[]
    prod=1
    for i in collection:
        prod*=i
        a.append(prod)
    print(a)
cumulative_product()