def is_unique(word):
    dictionary = {}
    for letter in word:
        if letter not in dictionary.keys():
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1

    for count in dictionary.values():
        if count > 1:
            return False

    return True


print(is_unique('abcde'))
print(is_unique('abcdeb'))
