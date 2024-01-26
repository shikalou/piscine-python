def all_thing_is_obj(object: any) -> int:
    t = object.__class__
    if (t is list):
        print("List :", t)
    elif (t is tuple):
        print("Tuple :", t)
    elif (t is set):
        print("Set :", t)
    elif (t is dict):
        print("Dict :", t)
    elif (t is str):
        print(f"{object} is in the kitchen", t)
    else:
        print("Type not found")
    return (42)
