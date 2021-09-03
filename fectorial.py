n = int(input("enter number"))
fec = 1

for x in range(1,n+1):
    fec = fec * x

print(fec)

'''

# using recursion

def fec(n):
    if n == 1:
        return 1
    else:
        return n * fec(n-1)
'''
