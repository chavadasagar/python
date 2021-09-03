def fibonacci(n):
    f = [0,1]
    n1=0
    n2=1

    for x in range(n):
        n3 = n1+n2
        f.append(n3)
        n1=n2
        n2=n3

    return f

n = int(input("enter no :"))
    
f = fibonacci(n)

print(f)
