######poem = open("rosalind_ini5.txt","r") 

#
#####for line in poem:
   #### if count %2 ==0:
   ###    poem = readlines(i).split('\n')
     #   print(line)
##



#def main(file):
 #   for i, line in enumerate(open("rosalind_ini5(1).txt").readlines()):
  #      if i % 2 == 1:
   #         print(line, end="")
    
    
f = open('/Users/maisievarcoe/Downloads/Python/Source Code/Rosalind-Challenges/Reading and writing/rosalind_ini5.txt', 'r')
g = open('AlwaysLookOnTheBrightSide', 'w')
for x in f.readlines()[1::2]:
  g.write(x)
  print(x)
g.close()


