# -*- coding: utf-8 -*-
def recurciveFn(idx):
    if idx >= 1:
        print(idx)
        idx = idx-1
        recurciveFn(idx)

recurciveFn(5)

print("차동화 천재")

print("특수문자==>"+"차동화\n천재천재천재")

print("문자타입==>"),
print(type("차동화"))

print("문자 반복==>"+"차동화 천재"*3)

print("인덱스 지정==>"+"karoscha jenius"[4])
print("역 인덱스 지정==>"+"karoscha jenius"[-4])

print("문자 구간 슬라이스==>"+"karoscha jenius"[3:5])
print("문자 구간 역 슬라이스==>"+"karoscha jenius"[-5:-3])
print("문자 구간 역 슬라이스 처음 파라미터만==>"+"karoscha jenius"[-5:])
print("문자 구간 슬라이스 두번째 파라미터만(OutOfRange없음)==>"+"karoscha jenius"[:100])
print("문자 구간 슬라이스 처음 파라미터만==>"+"karoscha jenius"[5:])
print("문자 구간 슬라이스 파라미터 없음==>"+"karoscha jenius"[:])

print("step test !!~~"[::3])
print("step test !!~~"[2::3])
print("step test !!~~"[2:9:3])
print("step test !!~~"[::-2])
print("step test !!~~"[::-1])
print("step test !!~~"[-1:-12:-1])

print("--{} {}--".format('차동화',452))
print("--{4} {3} {4} {3} {2} {1} {0} {1}--".format('차동화',452, 52.234, '천재', 'ㅋㅋㅋㅋ'))

print('karoscha'.upper())
print('KAROSCHA'.lower())

print('karoscha good'.find('good',3))
print('karoscha good'.find('good',12))

print('karoscha good pitch good'.count('good'))
print('karoscha good pitch good'.replace('good','nice'))

print('             dddd eeee           '.strip())
print('             dddd eeee           '.replace(' ',''))

print('karoscha|pitch|hana'.split('|'))

print("-".join('karoscha|pitch|hana'.split('|')))
print("/".join(['343','!@@##$$^','fffff']))

print("dfsdfsdfsdfsdf".count('df'))


