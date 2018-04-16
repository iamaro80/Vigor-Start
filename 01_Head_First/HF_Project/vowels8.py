def search4vowels(word: str) ->set:
    """Dispaly any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


search4vowels(input('Provide a word to search for vowels: '))