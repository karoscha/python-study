def showTuples(tu):
    for t in tu:
        print(t)

tuples = (1,2,3,4)

print(type(tuples))
print(tuples)

showTuples(tuples)

print(tuples[1])
print(tuples[-2])


print(tuples[2:4])
print(tuples[2:4]+tuples[0:2])
print(tuples.__contains__(5))

print(tuples.count(2))
print(tuples.__len__())