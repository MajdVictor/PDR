def intersection(nums1, nums2):
    #finding intersection
    return set(nums2).intersection(set(nums1))

if __name__ == "__main__":
    print(intersection([1,3,4,6,7,7], [3,4,10,20]))