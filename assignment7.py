import string
string1="The standard Lorem Ipsum passage, used since the 1500.\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt\nut labore et Dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation\n ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in\nreprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint\noccaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est\nlaborum."
list1=[]
sum=0
for i in string.ascii_lowercase:
    list1.append(i)

for y in list1:
    print(f"The count of {y}={string1.count(y)}")



for char in ["i","I"]:
    string1=string1.replace(char,"@")
print("\n",string1)


print("Number of statement=",string1.count("."))


word=string1.split()
for z in word:
    if z[0].isupper():
        sum+=1
print("Number of capital alphabets are ",sum)

dict1={"a":string1.count("a"),"e":string1.count("e"),"i":string1.count("i"),"o":string1.count("o"),"u":string1.count("u")}
print(dict1)