# my attempt knowing it would work but possibly lazy not the best way

# def vowel_counter(s: str) -> int:
#     vowels = 0
#     s = s.lower()
#     for i in s:
#         if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#             vowels += 1
#     print(vowels)

# vowel_counter('much more RELAXING')


# more consice and pythonic using list comprehension
def vowel_counter(s: str) -> int:
    return sum(1 for i in s.lower() if i in 'aeiou')

print(vowel_counter('much more RELAXING'))
