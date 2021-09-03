n = int(input("enter no"))
temp = 0
m = int(n/2)


for x in range(2,m):
    if(n%2 == 0):
        print("not prime no")
        temp = 1
        break

if(temp == 0):
    print("prime no")
