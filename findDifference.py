def findDifference(s, t):
    #solution 1 - faster than solution 2
    for i in s:
        if s.count(i) != t.count(i):
            return i
    return t[-1]


    #Solution 2
    #SOrting and iterating
    '''
    s = sorted(s)
    t = sorted(t)

    for i in range(len(s)):
    
        if s[i] != t[i]:
            return t[i]

    return t[-1]

    '''
    


if __name__ == "__main__":
    print(findDifference("abcdee","abcdeee"))