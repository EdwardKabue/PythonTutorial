from random import shuffle

def jumble(word):
    anagram = list(word) #generates a list of characters from a string provided
    shuffle(anagram)
    return ''.join(anagram)

words = ['beetroot', 'carrots', 'potatoes']
anagrams = [ ]

# for word in words:
#     anagrams.append(jumble(word))

# print(anagrams)

#print(list(map(jumble, words)))

print([jumble(word) for word in words])