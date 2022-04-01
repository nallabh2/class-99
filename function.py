f=open("test.txt")
fileLines=f.readlines()
introString="I am Abhi, I am 13 years old"
words=introString.split()
print(words)
for line in fileLines:
    print(line)