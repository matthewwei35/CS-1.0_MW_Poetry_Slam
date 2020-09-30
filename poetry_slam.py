def get_file_lines(filename):
    infile = open(filename, "r")
    read_poem = infile.readlines()
    infile.close()
    return read_poem

print(get_file_lines("Caged_Bird.txt"))