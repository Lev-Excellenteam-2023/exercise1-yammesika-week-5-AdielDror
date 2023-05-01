# The function accepts one or more iterable parameters, and returns a list of the interlaced elements
def interleave(*iterable):
    if not iterable:
        return None

    return [list(inner_loop.keys())[outer_loop] if type(inner_loop) is dict else inner_loop[outer_loop] for outer_loop
            in range(len(iterable[0])) for inner_loop in iterable]


# Version with generator
def interleave_generator(*iterable):
    return (list(inner_loop.keys())[outer_loop] if type(inner_loop) is dict else inner_loop[outer_loop] for outer_loop
            in range(len(iterable[0])) for inner_loop in iterable)


if __name__ == '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    print(interleave('abc', [1, 2, 3], ('!', '@', '#'), {6: 'd', 7: 'f', 8: 'g'}))
    print(interleave())
    for element in interleave_generator('abc', [1, 2, 3], ('!', '@', '#'), {6: 'd', 7: 'f', 8: 'g'}):
        print(element)
