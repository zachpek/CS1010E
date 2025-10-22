def flatten_with_depth(lst):
    # Returns (depth, value) pairs for each numerical data in the nested list, with 'top-level' elements having depth of 0

    def flattener(depth, data):
        if not data:
            return []
        elem = data[0]
        if type(elem) != list:
            return [(depth, elem)] + flattener(depth, data[1:])
        else:
            return flattener(depth + 1, elem) + flattener(depth, data[1:])

    return flattener(0, lst)

def process_nested_with_depth(ddata, pipeline):
    # Takes a list of depth-encoded data and applies a pipline of transformations to each depth-value pair, keeping the pair if the transformation does not return None
    for fn in pipeline:
        ddata = [fn(d, v) for d, v in filter(lambda x: x != None, ddata)]
    return ddata

def nested_from_depth(ddata):
    # terbalik sub-task 2a:
    # Turns a flattened list of depth-encoded data into a nested list of numerical data
    
    def insert_into_list(depth, value):
        if depth == 0:
            return value
        return [insert_into_list(depth - 1, value)]

    return [insert_into_list(d, v) for d, v in ddata]
