# Can build up a dict by starting with the empty dict {}
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

# print(dict)
# print(dict['a'])

dict['a'] = 6
# print(dict)

# if 'a' in dict: print(dict['a']) 
# print(dict.get('z'))

# By default, iterating over a dict iterates over its keys.
# Note that the keys are in a random order.
# for key in dict:
#   print(key)

# Exactly the same as above
# for key in dict.keys():
#   print(key)

# The methods dict.keys() and dict.values() return lists of the keys or values explicitly.
# print(dict.keys())
# print(dict.values())

# for key in sorted(dict.keys()):
#     print(key, dict[key])

#There's also an items() which returns a list of (key, value) tuples, which is the most efficient way to examine all the key value data in the dictionary.
# for k, v in dict.items():
#    print(k, '>', v)

#The "del" operator does deletions.
num = 6
del num #remove the definition of a variable, as if that variable had not been defined.

list = ['a', 'b', 'c', 'd']

del list[0]     ## Delete first element
del list[-2:]   ## Delete last two elements
#print(list)      ## ['b']

dict = {'a':1, 'b':2, 'c':3}
del dict['b']   ## Delete 'b' entry
#print(dict)      ## {'a':1, 'c':3}

#Files
#open file with a file handle that can be used to read a file in the usual way.
# f = open('foo.txt', 'rt', encoding='utf-8')

# for line in f:   ## iterates over the lines of the file
#     print(line, end='')  ## end='' so print does not add an end-of-line char since 'line' already includes the end-of-line.

# f.close() #use f.close() when finished.

#Files Unicode
with open('foo.txt', encoding='utf-8', mode='at') as f:
    f.write('\u20ACunicode\u20AC\n') 
    # AKA print('\u20ACunicode\u20AC', file=f)  ## which auto-adds end='\n'

