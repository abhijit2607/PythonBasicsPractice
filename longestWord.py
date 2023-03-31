def find_longest_word(word_list):
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

word_list =eval(input('Enter a list words:'))
longest_word = find_longest_word(word_list)

print(f"The longest word in the list is '{longest_word}'.")
