'''n=int(input("Enter a number:"))
count=0
while n>0:
    count+=1
    n=n//10
print(count)

n=int(input())
temp=n
s=0
while n>0:
    s+=(n%10)
    n=n//10
print(s)
print(sum(map(int, str(temp))))''' 
n=int(input())
even=odd=0
while n>0:
    if(n%2)==0:
        even+=1
    else:
        odd+=1
    n=n//10
print(even,odd)    
n=int(input())
 