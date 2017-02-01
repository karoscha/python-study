def printDic(dic):
    for key in dic.keys():
        print("key='{}', value='{}'".format(key,dic[key]))
def printDicValueList(valList):
    for v in valList:
        print("value='{}'".format(v))


dic = {1:'karoscha',2:'pidch','love':'karos love pidch'}
print(type(dic))
print(dic)

printDic(dic)

print(dic[1])
print(dic[2])
print(dic['love'])

dic['love'] = 'pidch love karoscha'
print(dic)

print(len(dic))
del dic['love']
print(dic)
print(len(dic))

printDic(dic)

printDicValueList(dic.values())