def ft_filter(function, iterable):
    filtered = [i for i in iterable if function(i)]
    return (filtered)
