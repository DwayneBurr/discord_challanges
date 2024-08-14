def longest_string(s):
    char_list = []
    longest_substring = 0

    for i in s:

        while i in char_list:

            char_list.pop(0)

        char_list.append(i)
 
        longest_substring = max(longest_substring, len(char_list))

    return longest_substring

print(longest_string("I have no idea how this is working"))

# for loop iterating through the list of characters (string)
# while the individual char (i) is inside the char list it will then remove (pop)
# the first instance of the char on the 0th index appending each iteration 
# basically sliding it to the left when the number comes back
#visual for personal rememberance: 1: abcdefabcdef ->  2: bcdefabcdefa -> 3: cdefabcdefab ->  4: defabcdefabc

# then the longest_substring check if the current max substring is higher than the previous max and replaces it
# so the longest substring will take the longest substring and the length of the character list will be compared 
# continuously in the for lop every iteration will compare the current longest substring with the current char_list