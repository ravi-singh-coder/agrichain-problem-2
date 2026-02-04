def longest_substring_without_repeating_characters(s):
    last_seen = {}
    start = 0
    max_length = 0
    for end in range(len(s)):
        char = s[end]


        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1


        last_seen[char] = end


        max_length = max(max_length, end - start + 1)

    return max_length



if __name__ == "__main__":
    user_string = input("Enter a string: ")
    result = longest_substring_without_repeating_characters(user_string)

    print("Length of longest substring without repeating characters:", result)
