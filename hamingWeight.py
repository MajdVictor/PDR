def hammingWeight(n):
    a=0
    for i in bin(n):
        if i == "1":
            a+=1
        
    return a

if __name__ == "__main__":
    print(hammingWeight(2))