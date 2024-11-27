def iterate_tree(target, parent_keys: = []):
    if type(target) == dict:
        tree_indexes = target.keys()
    elif type(target) in (list,tuple,range):
        tree_indexes = range(len(target))
    else:
        tree_indexes = None
    if tree_indexes == None:
        yield (parent_keys, target)
    else:
        for branch in tree_indexes:
            yield from iterate_tree(target[branch],parent_keys + [branch])