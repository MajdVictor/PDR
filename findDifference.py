def findDifference(s, t):
    #solution 1
    for i in s:
        if s.count(i) != t.count(i):
            return i
    return t[-1]


if __name__ == "__main__":
    print(findDifference("abcdee","abcdeee"))