
'''n = int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")    
print(n)
n=int(input())
count=0
for i in range(2,n//2+1):
    if n%i==0:
        count+=1
print("prime" if count==0 else "not prime") '''   
'''display all the prime numbers in the given range'''
'''start=int(input())
end=int(input())
if start==1:
    start=2
for n in range(start,end+1):
    count=0    
    for j in range(2,n//2+1):
        if n%i==0:
            count+=1
    if count==0:
        print(n,end=" ")'''
#GCD of two numbers
a=int(input())
b=int(input())
while b:
    a,b=b,a%b
print(a) 