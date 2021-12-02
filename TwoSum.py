'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

Time complexity less than O(n^2)
'''

def twoSum(listOfNumbers, target):

    d = {} #key = list element, value = index

    for index, val in enumerate(listOfNumbers):

        if target - val in d:
            return d[target - val], index

        d[val] = index





if __name__ == '__main__':

    list1 = [1,3,6,7,9]
    target1 = 13

    list2 = [4,1,5,2,10]
    target2 = 11


    print("First sample: ", twoSum(list1, target1))
    print("Second sample: ", twoSum(list2, target2))

