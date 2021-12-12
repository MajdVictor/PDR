def removeElement(nums,val):
    
    while val in nums:
        nums.remove(val)
    
    return len(nums)

if __name__ == "__main__":
    print(removeElement([1,1,4,3,6,7],1))