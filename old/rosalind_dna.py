s = ""
with open("./rosalind_dna.txt") as file:
    s = file.readline()

fd = {}
for char in s:
    fd[char] = fd.get(char, 0) + 1

print(fd)
    
