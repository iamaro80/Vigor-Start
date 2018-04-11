# Vowels version 3 (using dictionary instead of list)

vowels = ['a','e','i','o','u']

word = input("Provide a word to search for vowels: ")
#found = []
found = {} # change found to dict for counting

for vowel in vowels: # initialize dict keys to 0 
    found[vowel] = 0

for letter in word:
    if letter in vowels:
            found[letter] += 1 
        # if letter not in found:
        #     found.append(letter)

#print(found.items())

for k,v in sorted(found.items()): # sort the output 
    print(k,'was found',v,'times')

# for vowel in found:
#     print(vowel)

