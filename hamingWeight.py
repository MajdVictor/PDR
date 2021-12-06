def hammingWeight(n):
    a=0
    for i in bin(n):
        if i == "1":
            a+=1
        
    return a

def hammingWeight2(n):
    return bin(n).count("1") #Faster solution

if __name__ == "__main__":
    print(hammingWeight2(2))