# set, мнгджество, коптук.
# {1,2,3,4,4,4,4}
# add()
# pop()
# discard()
# remove()
# &
# update(дабавлять)
a = {1,2,3,4}
b = {4,5,6}
print( a | b) 
print(a & b)

print({int(i) for i in input().split()})

a = { i for i in input().split()}
print(a)

wor = [i for i in input().split()]
set_wor = set(wor)
res = []
for i in set_wor:
    res.append(wor.count(i))
print(wor)
print(set_wor)
print(res)

a = {1,2,3,4,5}
print(a.update([6,7,8,9]))