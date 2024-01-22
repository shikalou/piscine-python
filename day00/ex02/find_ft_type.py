def all_thing_is_obj(object: any) -> int:
    # t = type(object)
    t = object.__class__
    if (t is list):
        print("List :", t)
    if (t is tuple):
        print("Tuple :", t)
    if (t is set):
        print("Set :", t)
    if (t is dict):
        print("Dict :", t)
    if (t is str):
        if (object == "Brian"):
            print("Brian is in the kitchen", t)
        if (object == "Toto"):
            print("Toto is in the kitchen", t)
    if (t is int):
        print("Type not found")
    return (42)
