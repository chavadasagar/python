n = int(input("enter number :"))
rev = 0
temp_no = n
while n>0:
    rem = int(n%10)
    rev = int(rev*10+rem)
    n =   int(n/10)

if temp_no == rev:
    print(f"{temp_no} is pelindrome no")
else:
    print(f"{temp_no} is not pelindrome no")
