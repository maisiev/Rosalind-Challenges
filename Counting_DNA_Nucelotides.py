file = open('/Users/maisievarcoe/Downloads/Python/Source Code/Rosalind-Challenges/rosalind_dna.txt', 'r')
nucleotides = file.read()

base_count = [0, 0, 0, 0]
for base in nucleotides:
    base = base.strip('\n')
    if base == 'A':
        base_count[0] += 1 
    elif base == 'C':
        base_count[1] += 1   
    elif base == 'G':
        base_count[2] += 1
    elif base == 'T':
        base_count[3] += 1

for char in base_count:
        print(char, end=' ')  
file.close()

    # To split characters in a string when there's no space between them,
    # you can iterate through the string directly.
    # Example:


