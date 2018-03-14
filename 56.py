#56
m=input("Alphanumeric:")
v=0
a=0
for char in m:
    if(char.isdigit()):v=v+1
    if(char.isalpha()):a=a+1
    if(v>0 and a>0):
        print('yes')
        break
if(v==0 or a==0):print('No')
