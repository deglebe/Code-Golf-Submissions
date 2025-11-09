# init fib sequence starting values
a,b=0,1;r=[0,1]

# generate the next 47 fib numbers using exec and walrus as a psuedo-regex
# b := a + (a := b) ==> set a to be, set b to old_a + new_b, return new_b
exec("r+=[b:=a+(a:=b)];"*47)

# filter non-primes
# for each n in list r:
# - check n if prime
# - all non-zero remainders => n is prime
for n in r:all(n%i for i in range(2,n))or print(n)

