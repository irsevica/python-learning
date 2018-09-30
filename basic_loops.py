s = 'random_string'

for c in s:
    print(ord(c))

x=0
for c in s: x +=ord(c)

print(x)

ordlist = []
for c in s:
  ordlist.append(ord(c))

print(ordlist)

ordlist = map(ord, s)
print(ordlist)
ordist = [ord(c) for c in s]
print(ordlist)

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0
while i < len(L):
  if 2 ** X == L[i]:
    print('at index', i)
    break
  else:
    i = i+1

for i in L:
  sum = 2 ** X
  res = L.index(sum)
  if res:
    print('at index', res )
    break

res = [L.index(item) for item in L if 2 ** X == item]
print('at index', res)

for item in L:
  x = 2 ** item
  L.append(x)

print(L)