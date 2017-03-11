def file_length(file):
    DICT = open(file, 'r')
    length = len(DICT.readlines())
    DICT.close()
    return length
