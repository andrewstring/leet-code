num = [2,7,11,15]
target = 9

num_one = [3,2,4]
target_one = 6

def sum(arr, target):
    for index, num in enumerate(arr):
        diff = target - num
        if diff in arr and index != arr.index(diff):
            return [ index, arr.index(diff)]

print(sum(num, target))
print(sum(num_one, target_one))

