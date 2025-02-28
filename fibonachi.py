'''def F(x: int)->int:
    if(x==0):
        return 0
    if(x==1):
        return 1
    return F(x-1)+F(x-2)

p = [0,1]
n = int(input())
for _ in range(n-1):
    p.append(p[-1]+p[-2])
print(F(n),p[n])'''

'''def check(s: str)->bool:
    counter = 0
    for i in s:
        if(i=='('): counter+=1
        else: counter-=1
        if counter<0: return False
    return counter==0
s = input()
print(check(s))'''

'''def plus_one(n:list)->list:
    for i in range(len(n)-1,-1,-1):
        if(n[i]==9):
            n[i] = 0
        else:
            n[i]+=1
            return n
    return [1]+n

print(plus_one([int(i) for i in list(input())]))'''

'''def number_of_unique_characters(s: str)->dict:
    d = {}
    for i in s:
        if i in d.keys():
            d[i]+=1
        else: d[i] = 1
    return d
print(number_of_unique_characters(input()))'''

'''def two_sum(l:list, n:int)->list:
    s = set(l)
    for i in range(len(l)):
        if n-l[i] in s:
            return [i,l.index(n-l[i])]'''
'''
number = 1234567890
print(f"{number:^30,.3f}".replace(' ','*').replace(',',' '))
'''