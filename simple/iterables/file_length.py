def file_length(file):
    with DICT as open(file, 'r'):
        length = len(DICT.readlines())
    return length
