
##buble sort ---> O(n^2)
listOfNumbers = [20,2,10,3.3,15,7]

temp = 0 

for i in range(len(listOfNumbers)):
    for x in range (len(listOfNumbers) - i - 1):
        if listOfNumbers[x] > listOfNumbers[x+1]:
            temp = listOfNumbers[x+1]
            listOfNumbers[x+1] = listOfNumbers[x]
            listOfNumbers[x] = temp

print(listOfNumbers)