w = 'BANANA'
s = 0
k = 0
v =['A','E','I','O','U','Y']

for i in range(len(w)):
    if w[i] in v:
        k += len(w) -i
    else:
        s += len(w) -i

if s> k:
    print('Stuart',s)
else:
    print('Kevin', k)
        