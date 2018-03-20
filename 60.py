#60
n=int(input("Enter The Fibonacci Range"))
count = 0
a1 = 0
a2 = 1
l=[]
if n == 1:
    l.append(a1)
else:
    while count < n:
        l.append(a1)
        nth = a1 + a2
        a1 = a2
        a2 = nth
        count += 1
print(" ".join(str(x) for x in l))
