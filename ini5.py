

def main(file):
    for i, line in enumerate(open("rosalind_ini5.txt.txt").readlines()):
        if i % 2 == 1:
            print(line, end="")
    
