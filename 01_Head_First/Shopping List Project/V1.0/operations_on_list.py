import os

ev_key = 'tryout'
sl_path = ''

if os.getenv(ev_key) is None:
    print('not found')
    os.environ[ev_key] = 'xyx'
    sl_path = os.getenv(ev_key)
else:
    sl_path = os.getenv(ev_key)
    
print(sl_path, '(File directory)')

os.chdir(sl_path)


def is_sl_found(slname: str) ->bool:
    if read_all_sl():
        if slname in str(read_all_sl()).strip():
            return True
    else:
        return False


def add_sl(slname: str) ->str:
    if not is_sl_found(slname):
        with open('sl.txt', 'a') as sll:
            sll.write(slname+'\n')
        return slname
    else:
        return -1


# def read_all_sl() ->list:
#     sl = []
#     with open('sl.txt', 'r') as all_lists:
#         for i in all_lists:
#             sl.append(i.strip('\n'))
#     if sl:
#         return sl
#     else:
#         return False

def read_all_sl() ->list:
    if open_sl_file():
        return open_sl_file()
    else:
        return False


def open_sl_file() ->list:
    sl = []
    with open('sl.txt', 'r') as all_lists:
        for i in all_lists:
            sl.append(i.strip('\n'))
    return sl

# def rename_sl(slname: str) ->str:

print(add_sl('things'.strip()))
ssl = read_all_sl()
print(ssl)
