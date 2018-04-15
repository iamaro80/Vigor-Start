# using set over the list. the issue here that we can't count the number of the occurance because set doesn't 
# allow duplication. I think this is not the optimal solution if the number of occurance is a must

vowels = set('aeiou')

word = input("Provide a word to search for vowels: ")

found = vowels.intersection(set(word))

if len(found) > 0:
    for vowel in found:
        print(vowel)
else:
    print('No Vowel Found!')

