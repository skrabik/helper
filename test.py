d = {'a': 'adsf',
     'b': 'afsaf',
     'c': 'fasda',
     'v': 'dasadf',
}
el = int(input())
c = 1
for i in d:
     if c == el:
          del d[i]
          break
     c += 1

print(d)