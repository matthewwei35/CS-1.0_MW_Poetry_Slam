import random

# -----------------------------------------------
# Prints out the poem file into the terminal as a list
def get_file_lines(filename):
    infile = open(filename, "r")
    read_poem = infile.readlines()
    infile.close()
    return read_poem

print(get_file_lines("Caged_Bird.txt"))

# -----------------------------------------------
# Prints out the lines of the poem backwards
def lines_printed_backwards(lines_list):
    list_length = len(lines_list)
    lines_list = lines_list[::-1]

    for i in range(len(lines_list)):
        line_number = str(list_length - i) + " " + lines_list[i]
        print(line_number)

infile = open("Caged_Bird.txt", "r")
print(lines_printed_backwards(infile.readlines()))
infile.close()

# -----------------------------------------------
# Randomly prints out lines of the poem randomly
def lines_printed_random(lines_list):
    for random_line in range(len(lines_list)):
        random_line = random.choice(lines_list)
        print(random_line)

infile = open("Caged_Bird.txt", "r")
print(lines_printed_random(infile.readlines()))
infile.close()

# -----------------------------------------------
# Adds smiley faces to the poem lines
def lines_printed_smiley(lines_list):
    for i in range(len(lines_list)):
        smiley_line = ":)  " + lines_list[i] + "  (:"
        print(smiley_line)

infile = open("Caged_Bird.txt", "r")
print(lines_printed_smiley(infile.readlines()))
infile.close()
