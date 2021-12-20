def reverseString(str):

    #one solution
    # str[:] = str[::-1]

    # return str

    #Second solution

    start, end = 0, len(str)-1
    while start<end:
        str[start], str[end] = str[end], str[start]

        start += 1
        end -= 1

    return str

if __name__ == "__main__":
    print(reverseString(['h','e','l','l','o']))