# shopping_lists=['list1','list2']
# shopping_lists= {'id':0,'name':'list1','id':1,'name':'list2'}

# think of the combination of list and dict (try sorted and setdefault methods)
# units=['kg','liter']
units = {}
units['en'] = {'kg', 'liter', 'box', 'packet'}
units['ar'] = {'كيلو', 'لتر', 'صندوق', 'باكيت'}
units['fr'] = {'kg', 'litre', 'boîte', 'paquet'}


def call_unit_by_lang(lang: str='en') ->set:
    '''Return a set of units for specific language'''
    return set(units[lang])

x = call_unit_by_lang('fr')
print(sorted(x))


def add_unit_by_lang(lang: str, unit: str) ->str:
    '''Add unit to specific language units'''
    return units[lang].add(unit)


add_unit_by_lang('fr', 'unité')
print(call_unit_by_lang('fr'))
    

# print(call_unit_by_lang('en'))
# print(add_unit_by_lang('en', 'packet'))
# print(units['en'], 'add new unit to en')
# lang = call_unit_by_lang('en')
# print(type(lang), 'type of lang')
# print(lang, 'lang elements')
# #lang = units['en'].remove('packet')
# print(units['en'], 'remove unit from unit')

# item = {'name':'rice',
#         'amount':5,
#         'unit':units[0]
#         }

# print(shopping_lists)
# print(item)