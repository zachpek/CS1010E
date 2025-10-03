# Name: Pek Tze Hng, Zachary
# NUSNET ID: E1525681
# Question Number: 7

def fg7(tup, pred1, pred2):
    # given:
    # - one (possibly empty) tuple containing integers
    # - two preedicates (functions pred1 and pred2 returning either True or False)
    # fg7 processes the tuple such that:
    # 1. those integers in tup violating either condition pred1 or pred2 will be removed from the generated list;
    # 2. otherwise, these integers in tup will have their right-most digit kept in the generated list.
    # the relative ordering of the items in the resulting list is the same as the original input from tup.

    return [elem % 10 for elem in tup if pred1(elem) and pred2(elem)]
