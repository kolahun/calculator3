
#import statistics

collection = [99,86,87,88,111,86,103,87,94,78,77,85,86,120]
collection.sort()

print("soretd list=",collection)

mean = sum(collection)/len(collection)
print("Mean equals=",round(mean,3))

n=len(collection)
if n%2!=0:
    print("median=",collection[(n+1)//2-1])
elif n%2==0:
    print("median=",collection[(n//2)-1],collection[(n//2)])

#mode
#mode=statistics.mode(collection)
#print(mode)


#MODE
a=[]
b=[]
for i in collection: 
    for s in range(0,n):
        if collection[s] not in a:
            a.append(collection[s])
            
print(a)
for element in a:
    count1=collection.count(element)
    b.append(count1)
print("Mode =",a[b.index(max(b))])