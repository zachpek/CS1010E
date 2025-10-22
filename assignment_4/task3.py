def is_ancestor(name1, name2, pdict):
    # Checks if the person with name1 is an ancestor of the person with name2 in the parent dictionary pdict, returning True or False.
    
    parent = pdict.get(name2)
    while parent:
        if parent == name1:
            return True
        parent = pdict.get(parent)
    return False

def is_related(name1, name2, pdict):
    # Checks if the person with name1 is related to (i.e., shares a common ancestor) the person with name2 in the parent dictionary pdict, returning True or False.
    
    people1 = [name1]

    parent1 = pdict.get(name1)
    while parent1:
        people1.append(parent1)
        parent1 = pdict.get(parent1)

    parent2 = name2
    while parent2:
        if parent2 in people1:
            return True
        parent2 = pdict.get(parent2)

    return False
