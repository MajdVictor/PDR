def isPalindrome(str):

    for i in range(len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
        
    return True

def isPalindrome2(str):

    return str == str[::-1]

if __name__ == "__main__":
    print(isPalindrome2("abccba"))
