def strStr(haystack, needle):
    return haystack.index(needle) if needle in haystack else -1


def strStr1(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(strStr1("",""))
print(strStr1("j",""))