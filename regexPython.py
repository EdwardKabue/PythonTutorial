import re

str = 'purple alice@google.com, blah monkey alice@abc.com blah dishwasher'

alices = re.findall(r'aLiCe', str, flags = re.IGNORECASE)

# for alice in alices:
#     print(alice)


f = open("foo.txt", "r")
strings = re.findall(r'cons', f.read())

f.close()

for s in strings:
    print(s)