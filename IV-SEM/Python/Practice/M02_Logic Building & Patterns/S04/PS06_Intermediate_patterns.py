'''li=[1,2,3,4,5]
output:[2,4,6,8,10]
res=[]
for i in li:
    if i%2==0:
        res.append(i)
print(res)
print([i for i in li if i%2==0])
 #['a','b','c']=>"abc"
li1=['a','b','c']
res=""
for ch in li1:
   res+=ch
print(res)
print("".join(li1))  

 Intermediate patterns
1.Pyramid
n=4

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
2.inverted pyramid
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+" * "*i) 
3.Diamond 
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i) 
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)'''

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(j) for j in range(1,i+1)]))
n=int(input())
for i in range(1,n+1): 
    print(" "*(n-i)+" ".join([str(j) for j in range(i,0,-1)]))