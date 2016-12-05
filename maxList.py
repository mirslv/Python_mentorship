lines = [line.rstrip('\n') for line in open('file_to_read.txt')]
maxSumList = []
for a in lines:
    s = a.split(' ')
    localList = []
    for i in s:
        localList.append(int(i))

    if sum(maxSumList) <= sum(localList):
        maxSumList = localList

print sum(maxSumList)
print maxSumList