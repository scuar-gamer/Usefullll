#raqamlar yig'indisini topish uchun
a=input()
n=[]
for i in a:
    n.append(int(i))
print(sum(n))

#natural bo'luvchilarni topish uchun
n=int(input())
a=[]
for i in range(1, n+1):
    if n%i==0:
        a.append(i)
print(*a)

#tub ko'paytuvchilarga ajratish uchun
n=int(input())
s=[]
i=2
while i*i<=n:
    while n%i<1:
        s.append(i)
        n /= i
    i += 1
if n>1:
    s.append(i)
print(*s)
