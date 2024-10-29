'''num = [5,4,6,3,1,2]
#num.sort(reverse=False)
print(num)

n = sorted(num)
print(n)
'''

'''
num = [19,28,37,46,55,64,73]
sort_num = sorted(num,key=lambda x: x % 10)
print(sort_num)

names = ("Jyrgal", "Saule", "Aibarchyn", "Baiel", "Nurlis", "Bilal", "Arsen")
print(sorted(names, key=lambda x: len(x)))

names = ("Jyrgal", "Saule", "Aibarchyn", "Baiel", "Nurlis", "Bilal", "Arsen")

print(sorted(names, key=lambda x: x[1]))
print(sorted(names))

'''
a =  ['14','27','33','47','54','61','75']
#print(sorted(a,key = lambda x: int(x[0]) + int(x[-1]) ))


s = [99,121]
#print(list(lambda s: int(s[1][0]) + int(s[1][1])))
#print(int(s[1][0]) + int(s[1][2]))
print(s[0],'+ '[1])