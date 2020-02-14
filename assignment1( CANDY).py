n = int(input("total no of candies"))
m = int(input("no of candies to be omited"))
i=0
a=[]
print("u will eat the following candies")
while i<=n:
    print(i)

    a.append(i)
    i = (i+m)%n
    if i in a :
        print("no of candy ",len(a))
        break