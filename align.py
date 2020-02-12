import sys

match = 1
mismatch = -2
h = -5
g = -1

sequence_name = ""
sequence_string = ""
sequence_names = [""]
sequence_strings = []
whitespace = 0

with open("input", "r") as f:
    while True:
        f_content = f.readline()
        if ">" in f_content:
            whitespace = f_content.find(" ")
            sequence_name = f_content[1:whitespace]
            sequence_names.append(sequence_name)
            sequence_strings.append(sequence_string)           # sequence strings index start at 1
            sequence_string = ""                        # reset variable
            f_content = '\n'
        sequence_string += f_content.rstrip('\n')
        if not f_content:
            sequence_strings.append(sequence_string)
            break

n = len(sequence_strings[1])        #
m = len(sequence_strings[2])        #


placeholder = ""
print(f"Scores:   match = {match}, mismatch = {mismatch}, h = {h}, g = {g}")
print(f'Sequence 1 = "{sequence_names[1]}", length = {len(sequence_strings[1])} characters')
print(f'Sequence 2 = "{sequence_names[2]}", length = {len(sequence_strings[2])} characters')

print(sequence_strings[1])
print(sequence_strings)


#<executable name> <input file containing both s1 and s2> <0: global, 1: local> <optional: path to parameters config file>
