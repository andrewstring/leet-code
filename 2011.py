def finalValueAfterOperations(operations):
    return sum([1 if "+" in x else -1 for x in operations])

print(finalValueAfterOperations(["--X"]))
