import os
import pytest

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


def test_fileExists():
    assert os.path.isfile('file_to_read.txt')

def test_fileEmpty():
	assert os.path.getsize('file_to_read.txt') > 0