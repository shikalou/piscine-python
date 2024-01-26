def ft_filter(function, iterable):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    # print(ft_filter.__doc__)
    filtered = [i for i in iterable if function(i)]
    return (filtered)
