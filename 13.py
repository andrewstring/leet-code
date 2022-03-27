def romanToInt(str):
    numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    for i in range(len(str) - 1):
        if numerals[str[i]] < numerals[str[i + 1]]:
            res -= numerals[str[i]]
        else:
            res += numerals[str[i]]

    return res + numerals[str[-1]]

print(romanToInt("MCMXCIV"))