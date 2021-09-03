n = int(input("enter no :"))

t = 0

t_no = n
while n>0:
    rem = int(n%10)
    t = int(t+(rem*rem*rem))
    n = int(n/10)



if t_no == t:
    print("it is armstrong no")
else:
    print("it is not armstrong no")
