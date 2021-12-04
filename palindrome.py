#Finding Palindrome without usng strings

def isPalindrome(x):
        if x<0:
            return False
        else:
            n = x
            temp = 0
            while n:
                temp = temp*10 + n%10 
                n//=10
            return temp == x

if __name__ == "__main__":

    number = 234
    number2 = 234432


    print(isPalindrome(number))
    print(isPalindrome(number2))