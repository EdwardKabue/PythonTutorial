#Tuples are like lists, except they are immutable and do not change size (tuples are not strictly immutable since one of the contained elements could be mutable)
tuple = (1, 2, 'hi')

print(len(tuple))  ## 3
print(tuple[2])    ## hi

#To create a size-1 tuple, the lone element must be followed by a comma.
tuple = ('hi',)

#Assigning a tuple to an identically sized tuple of variable names assigns all the corresponding values. If the tuples are not the same size, it throws an error. This feature works for lists too.
(x, y, z) = (42, 13, "hike")
print(z)  ## hike
