def NULL_not_found(object: any) -> int:
    # t = type(object)
    t = object.__class__
    # print(t)
    if (object is None):
        print("Nothing:", object, t)
    elif (t == float):
        print("Cheese:", object, t)
    elif (object == 0 and t is int):
        print("Zero:", object, t)
    elif (object == ''):
        print("Empty:", t)
    elif (not object):
        print("Fake:", object, t)
    elif (t is str):
        print("Type not Found")
        return (1)
    return(0)