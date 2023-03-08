with open("rosalind_gc.txt") as file:
    curr_string = ""
    lables = []
    sequences = []
    for line in file:
        if line[0] == '>':
            if curr_string != "":
                sequences.append(curr_string)
            lables.append("".join([char for char in line][1:-1]))
            curr_string = ""
        else:
            curr_string += "".join([char for char in line][:-1])
    sequences.append(curr_string)

# breakpoint()

out_len = len(lables)
gc_content = [0 for _ in range(out_len)]
for idx in range(out_len):
    gc_count = 0
    for char in sequences[idx]:
        if char == "G" or char == "C":
            gc_count += 1
    gc_content[idx] = (gc_count / len(sequences[idx]))*100

max_label, max_percentage = "", 0
for idx in range(out_len):
    if gc_content[idx] > max_percentage:
        max_label = lables[idx]
        max_percentage = gc_content[idx]

print(max_label)
print(max_percentage)
