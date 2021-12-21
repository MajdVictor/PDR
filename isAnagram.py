def isAnagram(s , t):

    if len(s) != len(t):
        return False
    else:
        for i in s:
            if s.count(i) != t.count(i):
                return False
        return True

if __name__ == "__main__":
    print(isAnagram("cat","tacd"))