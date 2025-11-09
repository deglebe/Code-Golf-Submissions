a,b=0,1;r=[0,1]
exec("r+=[b:=a+(a:=b)];"*47)
for n in r:all(n%i for i in range(2,n))or print(n)
