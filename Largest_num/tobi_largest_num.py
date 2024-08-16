def longes(l:list) -> list:
    return "".join(sorted([i for i in "".join([str(int(j)) for j in l])]))[::-1]
print(longes([1, 20, 23, 4, 8]))

