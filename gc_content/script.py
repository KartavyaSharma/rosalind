with open("rosalind_gc.txt") as file:
    curr_string = ""
    lables = []
    sequences = []
    for line in file:
        if line[0] == '>':
            if curr_string != "":
                sequences.append(curr_string)
            lables.append(line.rstrip()[1:])
            curr_string = ""
        else:
            curr_string += line.rstrip()
    sequences.append(curr_string)

gc_content = []
for idx in range(len(lables)):
    gc_count = sum([1 for char in sequences[idx] if char == "G" or char == "C"])
    gc_content.append((lables[idx], (gc_count / len(sequences[idx]))*100))

gc_content.sort(key=lambda x: x[1])

print(gc_content[-1][0])
print(gc_content[-1][1])
