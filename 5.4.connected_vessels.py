# The function accepts one or more iterable parameters, and returns a list of the interlaced elements
def interleave(*iterable):
    if not iterable:
        return None
    res = []
    j = 0

    # If we haven't reached the end of the first element
    # - assuming that the size of all elements is the same
    while j < len(iterable[0]):
        for i in iterable:
            if type(i) is dict:  # Checking if the element is a dictionary
                res += [list(i)[j]]

            else:
                res += [i[j]]
        j += 1
    return res


# Version with generator
def interleave_generator(*iterable):
    j = 0
    while j < len(iterable[0]):
        for i in iterable:
            if type(i) is dict:
                yield list(i)[j]
            else:
                yield i[j]
        j += 1


print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
print(interleave('abc', [1, 2, 3], ('!', '@', '#'), {6: 'd', 7: 'f', 8: 'g'}))
print(interleave())
for element in interleave_generator('abc', [1, 2, 3], ('!', '@', '#'), {6: 'd', 7: 'f', 8: 'g'}):
    print(element)
