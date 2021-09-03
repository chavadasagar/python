n = int(input("prime number :"))

m = int(n/2);
temp = 0
x=2
for x in range(m):
    if(x%n == 0):
        print("not prime no")
        temp = 1
        break

if(temp == 0):
    print("prime no")
