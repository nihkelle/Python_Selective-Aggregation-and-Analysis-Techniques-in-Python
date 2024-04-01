#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Nihkelle Scott


# In[ ]:


# Code 1
cList = [9, 4, 7, 3, 8]
cTuple = [5, 4, 3, 5, 2]
productList = []
listLen = len(cList)
loopIndex = 0
while loopIndex < listLen:
    productOfPair = cList[loopIndex] * cTuple[loopIndex]
    productList.append(productOfPair)
    loopIndex += 1
total = 0 
loopIndex = 0 
while loopIndex < listLen:
    total += productList[loopIndex]
    loopIndex += 1
print(total)


# In[ ]:


# Code 2
def buildMultTable():
    mulTable = []
    for outerLoop in range(10):
        currentLine = []
        for innerLoop in range(10):
            product = outerLoop * innerLoop
            currentLine.append(product)
        mulTable.append(currentLine)
    return mulTable
mt = buildMultTable()
for row in mt:
    print(row)


# In[ ]:


# Code 3
def sumMiddle(dataList):
    lengthOfList = len(dataList)
    sliceToSum = dataList[1:lengthOfList - 1]
    middleSum = sum(sliceToSum)
    dataList[1:lengthOfList - 1] = [middleSum]
def program():
    myList = [2, 4, 6, 8, 10]
    print(myList)
    sumMiddle(myList)
    print(myList)
program()

