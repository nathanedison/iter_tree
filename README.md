This function iterates through a tree consisting of any combination of dicts, lists, tuples, and ranges,
returning a generator that provides the index path to each leaf as well as its value.

The first argument (target) should be a dict, list, or tuple. The second argument (parent_indexes) should
not be used when calling the function; it is only needed for the recursion. The format of the output is a
2-length tuple containing (1) the list of indexes and (2) the value of the leaf: ([list,of,indexes],value)

The index_filters parameter is an optional dictionary for filtering indexes based on a boolean callable.
The keys of the dictionary specify the dimension number (starting at '1'). The values contain the boolean
callables to filter the specified dimensions. E.g.: {'1':callable,'3':callable}

The optional dim_limit parameter sets the deepest dimension to iterate (counting from 1).

The parent_keys parameter should not be used; its only purpose is to facilitate recursion of the function.
