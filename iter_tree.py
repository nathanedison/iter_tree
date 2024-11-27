# Iterates through a tree consisting of dicts, lists, and/or tuples
# Returns a generator that provides the index path to each leaf as well as its value.

# The index_filters parameter is an optional dictionary for filtering the indexes in one or more dimensions.
# The keys of the dictionary specify the dimension number (starting at 1).
# The value contains the boolean callable to filter that dimension.
# The optional dim_limit parameter sets the deepest dimension to iterate.
# The parent_keys parameter should not be used; its only purpose is to facilitate the recursion.
def iterate_tree(target, index_filters: dict = {}, dim_limit: int = 0, parent_keys: list = []):
    if type(target) == dict:
        branch_indexes = target.keys()
    elif type(target) in (list,tuple,range):
        branch_indexes = range(len(target))
    else:
        branch_indexes = None
    dimension = len(parent_keys) + 1
    if branch_indexes == None or dimension > dim_limit > 0:
        yield (parent_keys, target)
    else:
        if str(dimension) in index_filters.keys():
            branch_filter = index_filters[str(dimension)]
            if callable(branch_filter):
                branch_indexes = filter(branch_filter,branch_indexes)
        for branch in branch_indexes:
            yield from iterate_tree(target[branch], index_filters, dim_limit, parent_keys + [branch])