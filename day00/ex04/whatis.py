import sys

def checknumber(object: str) -> bool:
    try:
        float(object)
        return (True)
    except:
        return (False)

try:
    assert len(sys.argv) != 1, ""
    assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"
    assert checknumber(sys.argv[1]), "AssertionError: argument is not an integer"
    print("I'm Even." if int(sys.argv[1]) % 2 == 0 else "I'm Odd.")

except AssertionError as msg:
    print(msg)
