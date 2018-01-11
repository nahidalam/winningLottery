'''
Runs on Python 3.x
Author: Nahid Alam
'''

totalExpectedNum = 7

def findTicket(numStr):
    numListList = [list(map(int, x)) for x in numStr]
    for l in numListList:
        length = len(l)
        if length <7 or length > 14:
            continue
        res = []  #result list containing the result
        dfs(l, res, 0)
        if res:
            #print result in the desired format
            str1 = ''.join(list(map(str, l)))
            str2 = ' '.join(list(map(str, res)))
            toPrint = str1 + '->' + str2
            print(toPrint)


def dfs(numList, res, index):
    if index == len (numList):
        if len(res) == totalExpectedNum:
            return res
        else:
            return  []  #return an empty list
    if index < len(numList) and len(res) == totalExpectedNum:
        #we already have 7 items in the result list but the string contains more number
        #failed case so return an empty list
        return []


    num1 = numList[index] #num1 is the 1 digit number
    if num1 >=1 and num1 <=59 and (num1 not in res):
        res.append(num1)
        result = dfs(numList, res, index+1)
        if result: #result is not empty
            return result
        res.remove(num1)
    if index < len(numList) - 1:
        num = numList[index] * 10 + numList[index+1] #num is a 2 digit number
        if num >=1 and num <=59 and (num not in res):
            res.append(num)
            result = dfs(numList, res, index+2)
            if result: #result is not empty
                return result
            res.remove(num)

if __name__ == '__main__':
    numStr = ["569815571556", "4938532894754", "1234567", "472844278465445"]
    findTicket(numStr)
