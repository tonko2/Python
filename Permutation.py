def permutations(list):
    n = len(list)
    if n == 1:
        return [list]

    res = []
    for x in range(n):
        pivot = list[x]
        left_plus_right = list[0:x] + list[x+1:n]
        for y in permutations(left_plus_right):
            merged_list = [pivot] + y
            res.append(merged_list)

    return res

list = ['a', 'b', 'c']
print(permutations(list))