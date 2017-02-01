def listSearch(lst):
    for e in lst:
        if(type(e) == list):
            listSearch(e)
        else:
            print('list idx={} in element={}'.format(lst.index(e),e))
            print('list idx={0} in element={1}'.format(lst.index(e),e))
            print('list idx={1} in element={0}'.format(lst.index(e),e))

lst = [1,2,3,4,5,6,7,8]
print(lst)

listSearch(lst)

lst2 = [1,2,3,['c','b','a'],'fe','eee']

listSearch(lst2)

print(lst2[1:4])
print(lst2[:4])
print(lst2[2:])
print(lst2[:])
print(lst2[3][1])

lst3 = ['a','b','c','d',1,2,3]

print(lst3*3)
lst3[1]=4
print(lst3)
print(lst3+lst2)

lst4 = ['karos','pidch','lek']
lst4.append('my love')
print(lst4)
lst4.insert(1,'my love')
print(lst4)

lst5 = ['d','c','b','a']
lst5.extend([1,2,3,4])
print(lst5)

lst5.extend(lst2)
print(lst5)
print(lst5.index(3,7,11))

print(lst5.count(1))

print(lst5.pop())
print(lst5)
print(lst5.pop(3))
print(lst5)
lst5.remove(3)
print(lst5)

lst5.sort()
print(lst5)