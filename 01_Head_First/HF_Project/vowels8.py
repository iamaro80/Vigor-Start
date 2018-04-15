def search4vowels():
    vowels = set('aeiou')

    word = input("Provide a word to search for vowels: ")

    found = vowels.intersection(set(word))

    if len(found) > 0:
        for vowel in found:
            print(vowel)
    else:
        print('No Vowel Found!')

search4vowels()