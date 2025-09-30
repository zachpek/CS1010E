def cumsum_list(lst):
    result = []
    sum_so_far = 0
    for e in lst:
        sum_so_far += e
        result.append(sum_so_far)
    return result

def cumsum_list_comprehension_revision_last_week(lst):
    return [sum(lst[:i + 1]) for i in range(len(lst))]