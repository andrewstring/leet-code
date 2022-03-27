from doctest import OutputChecker


def longestCommonPrefix(str_list):
    length = min([len(str) for str in str_list])
    prefix = ""
    for i in range(length):
        checker = [str[i] for str in str_list]
        if checker.count(str_list[0][i]) == len(str_list):
            prefix += str_list[0][i]
        else:
            break

    return prefix



def longest(str_list):
    if not str_list:
        return ""
    min_str = min(str_list, key=len)
    for i, ch in enumerate(min_str):
        for str in str_list[1:]:
            if str[i] != ch:
                return min_str[:i]

print(longest(["cir", "car"]))
print(longestCommonPrefix(["flower", "flow", "flight"]))

if not []:
    print("yes")