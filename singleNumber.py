def singleNumber(listOfNumbers):

    d = {}
    for i in listOfNumbers:
        if i not in d:
            d[i] = i
        else:
            del d[i]
    return list(d.keys())[0]

def singleNumber2(listOfNumbers):

    '''
    This solution uses the XOR bit operation
    '''
    #bitwise operation ( XOR )
    xorResult = 0
        
    for i in listOfNumbers:
        xorResult = xorResult ^ i
    return xorResult

if __name__ == "__main__":
    print(singleNumber2([1,1,2,3,4,3,4]))