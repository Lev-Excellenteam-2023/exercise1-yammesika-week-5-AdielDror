# The function accepts an unlimited number of lists and an option for an additional parameter,
# and concatenates them into one list and the additional parameter between them
def join(*lists, sep='-'):
    if not lists:  # If no lists were received at all
        return None
    separated = [sep]
    result_list = []
    # Concatenate the lists into one list with the 'sep' parameter between them
    for current_list in lists:
        result_list += current_list + separated
    result_list.pop()
    return result_list


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
