def isPalindrome(x):
    if x < 0:
        return False

    checker = 0
    copy = x
    while copy > 0:
        checker = checker * 10 + copy % 10
        copy //= 10

    return x == checker


def isPalindromeString(x):
    if x < 0:
        return False
    
    return str(x) == str(x)[::-1]

print(isPalindrome(232))
print(isPalindrome(2323))
print(isPalindromeString(232))
print(isPalindromeString(2323))