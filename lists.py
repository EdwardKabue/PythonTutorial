from operator import itemgetter

strs = ['aa', 'BB', 'zz', 'CC']
#sort list
#print(sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
#print(sorted(strs, reverse=True))   ## ['zz', 'aa', 'CC', 'BB']

#sort list based on function that generates proxy values that are used to sort.
strs = ['ccc', 'aaaa', 'd', 'bb']
#print(sorted(strs, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']

strs = ['aa', 'BB', 'zz', 'CC']
#print(sorted(strs, key=str.lower))

strs = ['xc', 'zb', 'yd' ,'wa']

#sort list based on custom function that generates proxy values that are used to sort.
def myFn(s):
    return s[0]

#print(sorted(strs, key=myFn))

#sorting by last name then by first name
grade = [('Freddy', 'Frank', 3), ('Anil', 'Frank', 100), ('Anil', 'Wang', 24)]
#print(sorted(grade, key=itemgetter(1,0)))

#sorting by first name then by number score
#print(sorted(grade, key=itemgetter(0,-1)))

#the sort() method on a list sorts that list into ascending order. The sort() method changes the underlying list and returns None.
alist = [4,7,3,2,1,6]
alist.sort()
print(alist)

