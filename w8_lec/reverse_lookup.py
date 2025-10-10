# BOOOO DUN USE TYPE NAMES HERE def reverse_lookup(dict, val):
def reverse_lookup(dic, val):
    for k, v in dic.items():
        if v == val:
            return k

def reverse_lookup_koklim(dic, val):
    for key in dic:
        if dic[key] == val:
            return key
    return None
