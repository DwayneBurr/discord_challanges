input = [7, 34, 9]
# input = [8, 1, 4]

# first attempt
# sort_list = sorted(input, reverse=True)

# res = ''.join(str(n) for n in sort_list)

# print(res)

# refactor # 1
# sort = ''.join(str(n) for n in sorted(input, reverse=True))

# print(sort)

# spent some time making it better for a second time
# def longest(input: list[int]) -> str:
#     sort = ''.join(str(n) for n in sorted(input, reverse=True))
#     return sort
# res = longest(input)
# print(res)

#sort numbers individually from largest to smallest
def largest(input: list[int]) -> str:
    digits = []
    for i in input:
        for d in str(i):
            digits.append(d)

    sort_digits = sorted(digits, reverse=True)
    sort_digits = ''.join(sort_digits) 
    return sort_digits

res = largest(input)
print(res)