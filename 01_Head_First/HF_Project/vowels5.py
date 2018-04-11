# Vowels version 5 

vowels = ['a','e','i','o','u']

word = input("Provide a word to search for vowels: ")

found = {} # change found to dict for counting

for letter in word:
    if letter in vowels:
        # initialize dict on run time with setdefault method
        found.setdefault(letter,0) # .setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
        found[letter] += 1

for k,v in sorted(found.items()): # sort the output 
    print(k,'was found',v,'times')
print(found)
