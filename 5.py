def palindrome_1(str):

    length = len(str)
    output = ""
    if length < 2:
        return str

    for i in range(length):

        odd = extend(str, i, i)
        even = extend(str, i, i + 1)

        output = odd if len(odd) > len(output) else output
        output = even if len(even) > len(output) else output
        
    return output




    

def extend(str, i, j):

    while(i >= 0 and j < len(str) and str[i] == str[j]):
        i -= 1
        j += 1

    return str[i + 1: j]


print(palindrome_1("cbbd"))