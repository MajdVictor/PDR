def isAnagram(s , t):

    if len(s) != len(t):
        return False
    else:
        ##set is used since there's no need to count same letter multiple times if occured, -> best performance
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True


if __name__ == "__main__":
    print(isAnagram("cat","tacd"))