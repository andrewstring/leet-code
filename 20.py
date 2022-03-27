def isValid(str):
    parenthesis = {")":"(", "]":"[", "}":"{"}
    paren = []
    for char in str:
        if char in parenthesis.values():
            paren.append(char)
        elif char in parenthesis.keys():
            if paren == [] or parenthesis[char] != paren.pop():
                return False

    return paren == []

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("[(])"))
print(isValid("[()]"))