def reverseString(str):

    #one solution
    str[:] = str[::-1]

    return str

if __name__ == "__main__":
    print(reverseString(['h','e','l','l','o']))