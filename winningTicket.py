totalCount = 7
maxTensDigit = '5'
allowedChars = ['0','1','2','3','4','5','6','7','8','9']
prevChar = ''
res = []

def findTicket(numStr):
    global prevChar
    for currStr in numStr:
        length = len(currStr)
        if length <7 or length > 14:
            continue
        for i in range (len(currStr)):
            currChar = currStr[i]
            if currChar not in allowedChars:
                print("Input must be a char in the range of 0-9")
                break
            elif currChar == '0':

                continue
            elif prevChar:
                #we have enough characters to create a two digit number
                addToList(currChar)
            elif currChar > maxTensDigit:
                #current number >5, we can't form a two digit number
                addToList(currChar)
            elif len(currStr) - i == totalCount - len(res):
                addToList(currChar)
            else:
                prevChar = currChar
        #if len(res) != 7:
        #    continue
        print (res)


def addOneDigitChar(currChar):
    global prevChar
    num = int(currChar)
    if num not in res:
        res.append(num)
    prevChar = ''


def addTwoDigitChar(currChar):
    global prevChar
    numTwoDigit = int(prevChar+currChar)
    if numTwoDigit not in res:
        res.append(numTwoDigit)
        prevChar = ''
    else:
        #the combined number already exists in the list
        #so use the prevChar to add an one digit number to the list
        addOneDigitChar(prevChar)
        if currChar > maxTensDigit:
            addOneDigitChar(currChar)
        else:
            prevChar = currChar


def addToList(currChar):
    if prevChar:
        addTwoDigitChar(currChar)
    else:
        addOneDigitChar(currChar)


if __name__ == '__main__':
    #numStr = [ "569815571556", "4938532894754", "1234567", "472844278465445"]
    numStr = [ "4938532894754", "1234567"]
    findTicket(numStr)
