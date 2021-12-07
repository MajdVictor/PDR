def singleNumber(listOfNumbers):

    d = {}
    for i in listOfNumbers:
        if i not in d:
            d[i] = i
        else:
            del d[i]
    return list(d.keys())[0]

if __name__ == "__main__":
    print(singleNumber([1,1,2,3,4,3,4]))