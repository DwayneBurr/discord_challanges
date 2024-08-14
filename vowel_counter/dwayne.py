def vowel_counter(s: str) -> int:
    vowels = 0
    s = s.lower()
    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowels += 1
    print(vowels)

vowel_counter('much more RELAXING')
