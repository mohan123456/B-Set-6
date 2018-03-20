#58
a,b=map(int,input("Enter The Two values:").split(' '))
a = a ^ b;
b = a ^ b;
a = a ^ b;
print(a,b)
