def isPalindrome(str):

    
    for i in range(len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
        
    return True

if __name__ == "__main__":
    print(isPalindrome("abccbaq"))
