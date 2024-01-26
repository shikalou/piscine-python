def NULL_not_found(object: any) -> int:
    t = object.__class__
    if (object):
        if (object != object):
            print("Cheese:", object, t)
        else:
            print("Type not found")
    elif (object is None):
        print("Nothing:", object, t)
    elif (object == 0 and t is int):
        print("Zero:", object, t)
    elif (object == ''):
        print("Empty:", t)
    elif (not object):
        print("Fake:", object, t)
    return (0)
