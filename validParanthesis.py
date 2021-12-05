def validParanth(s):
    

    d = {
        "(":")",
        "{":"}",
        "[":"]"
        }

    lstack = []

    for i in s:
        if i in "({[":
            lstack.append(i)
        else:
            if lstack:
                if i == d[lstack[-1]]:
                    lstack.pop()
                else:
                    return False
            else:
                return False

    return lstack == []

if __name__ == "__main__":
    s = "{[]]}"
    print(validParanth(s))
