def search4vowels(word: str) ->set:
    """Dispaly any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


search4vowels(input('Provide a word to search for vowels: '))


def search4letters(phrase: str, letters: str='aeiou') ->set:
    """Return a set  of the 'letters' found in phrase"""
    return set(letters).intersection(set(phrase))


print(search4letters('''Lorem ipsum dolor sit amet,consectetur adipiscing elit. 
                    Proin luctus imperdiet lectus, in varius tortor porta in. 
                    Sed maximus tincidunt ex, non porta dui blandit eu. Nullam 
                    facilisis libero vitae felis semper, nec laoreet tortor 
                    condimentum. Nunc facilisis tempus ex vel laoreet. Sed 
                    luctus quam nisi, id blandit turpis porta vel. Donec 
                    iaculis aliquam ex. Nullam luctus ac leo vel 
                    convallis.'''))