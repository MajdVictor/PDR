#encoded[i] = arr[i] XOR arr[i + 1]
def decode(encodedList, first):
        l = [first]
        
        for i in encodedList:
            l.append(l[-1] ^ i)
        return l

if __name__ == "__main__":
    print(decode([1,2,3], 1))