# The function accepts an unlimited number of lists and an option for an additional parameter,
# and concatenates them into one list and the additional parameter between them
def join(*lists, sep='-'):
    if not lists:  # If no lists were received at all
        return None
    lst = [sep]
    res = []
    # Concatenate the lists into one list with the 'sep' parameter between them
    for list1 in lists:
        res += list1 + lst
    res.pop()
    # print(res)
    return res


join([1, 2], [8], [9, 5, 6], sep='@')
join([1, 2], [8], [9, 5, 6])
join([1])
join()
