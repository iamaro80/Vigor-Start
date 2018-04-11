# Vowels version 4 

vowels = ['a','e','i','o','u']

word = input("Provide a word to search for vowels: ")

found = {} # change found to dict for counting

for letter in word:
    if letter in vowels:
        # initialize dict on run time
        if letter in found:         
            found[letter] += 1 
        else:
            found[letter] = 1

for k,v in sorted(found.items()): # sort the output 
    print(k,'was found',v,'times')

