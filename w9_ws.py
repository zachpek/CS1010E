# part 2 anagram

def is_anagram(word1, word2):
    letter_frequencies_1 = {}
    letter_frequencies_2 = {}
    for letter in word1:
        if letter != ' ':
            if letter not in letter_frequencies_1:
                letter_frequencies_1[letter] = 1
            else:
                letter_frequencies_1[letter] += 1
    for letter in word2:
        if letter != ' ':
            if letter not in letter_frequencies_2:
                letter_frequencies_2[letter] = 1
            else:
                letter_frequencies_2[letter] += 1
    return letter_frequencies_1 == letter_frequencies_2

# part 3 T9

def to_dict(keyL):
    dict_mapping = {}
    for i in range(len(keyL)): # len(keyL) should really be 10
        for char in keyL[i]:
            dict_mapping[char] = i
    return dict_mapping

def to_list(keyD):
    lst_rep = [''] * 10
    for k, v in keyD.items():
        lst_rep[v] += k
    return lst_rep

def to_nums(word):
    keypad_mapping = to_dict([' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'])
    nums_to_press = 0
    for char in word:
        nums_to_press *= 10
        nums_to_press += keypad_mapping[char]
    return nums_to_press  
