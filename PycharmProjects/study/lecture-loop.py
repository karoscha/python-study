idx = -1
while idx < 5:
    idx += 1
    if idx == 3:
        break
    elif idx%2 == 0:
        continue
    else:
        print('idx={}'.format(idx))

lst = ['a','b','c','d']

for e in lst:
    print(e)

for e in range(10):
    print('val={}'.format(e))

for idx in range(10):
    for kdx in range(10):
        print('idx={}, kdx={}'.format(idx,kdx))