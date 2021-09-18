n=int(input())
m=int(input())
l=float(input())
c=1
k=1
t=n
while n>0:
    if n==1:
        break
    n-=k
    c=c*2

for i in range(1,t+1):
    end=(i*(i+1)//2)
    print(end)
    if m<=end:
        lst=end
        frst=end-i+1
        print(lst,frst)
        break
print(m,lst,frst)
if m==lst or m==frst:
    print(n/c)

else:
    print(n/c*2)
