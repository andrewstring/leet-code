def longest_initial(s):
    max = 0
    counter = 0
    length = len(s)
    index = 0
    start = 0
    char_holder = set()
    char_holder_str = ""

    while index < length:
        if not s[index] in char_holder:
            char_holder.add(s[index])
            char_holder_str += s[index]
            index += 1
            counter += 1
        else:
            if counter > max:
                max = counter
            counter = 0
            inner_index = char_holder_str.find(s[index])
            start += (inner_index + 1)
            index = start

            char_holder = set()
            char_holder_str = ""

        if counter > max:
            max = counter
    return max


print(longest_initial("abcabcde"))

# Faster Solution
def longest(s):
    l = 0
    output = 0
    seen = {}

    for i in range(len(s)):
        if s[i] not in seen:
            output = max(output, i - l + 1)
        else:
            if seen[s[i]] >= l:
                l = seen[s[i]] + 1
            else:
                output = max(output, i - l + 1)
        seen[s[i]] = i
    return output
        

print(longest("abcjkllsl"))
