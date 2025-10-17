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

def is_anagram_khoo(w1, w2):
    d1 = {}
    d2 = {}
    for c in w1:
        if c in ' \t\n':
            continue
        d1[c] = d1.get(c, 0) + 1 # second argument of dict.get is the value to return if key is not found
    for c in w2:
        if c in ' \t\n':
            continue
        d2[c] = d2.get(c, 0) + 1
    return d1 == d2

def is_anagram_khoo_2(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    d1 = {}
    d2 = {}
    for c in w1:
        if ord('a') <= ord(c) <= ord('z'):
            d1[c] = d1.get(c, 0) + 1
    for c in w2:
        if ord('a') <= ord(c) <= ord('z'):
            d2[c] = d2.get(c, 0) + 1
    return d1 == d2

# part 3 T9

def to_dict(keyL):
    dict_mapping = {}
    for i in range(len(keyL)): # len(keyL) should really be 10
        for char in keyL[i]:
            dict_mapping[char] = i
    return dict_mapping

def to_list(keyD):
    # lst_rep = [''] * 10 # no good for variable len(keyL)
    lst_rep = [''] * (max(keyD.values()) + 1)
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

def to_nums_python(word):
    keypad_mapping = to_dict([' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'])
    num = ''
    for char in word:
        num += str(keypad_mapping[char])
    return int(num)
