#make dictionary of words and how many times theyre said
#read the file and split each word by spaces and then add each word to dictionary, if already in, count + 1

def main():
    file = open('/Users/maisievarcoe/Downloads/Python/Source Code/Rosalind-Challenges/rosalind_ini6.txt', 'r')
    words = file.read().split()
    dic = {}
    for word in words:
        word = word.strip('\n')
        if word in dic:
            dic[word] += 1 
        else:
            dic[word] = 1
    for key, value in dic.items():
        print(key, end=' ')
        print(value)   
    file.close()
    return       

class Person:
    def __init__(self, name,age):
        self.name = name  # Initialize the 'name' attribute
        self.age = age  # Initialize the 'name' attribute

# Create an object of the class
obj = Person("Maisie", 22)
print(obj.name)  # Output: Maisie

# create an array of class type person 



if __name__  == "__main__":
    main()


  




