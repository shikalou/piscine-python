import sys
import re
from ft_filter import ft_filter


def string_filter(S) -> bool:
    if (len(S) > int(sys.argv[2])):
        return (True)
    return (False)


def main():
    """
    The script selects elements from a list based on the output of a function.

    The function is applied to each element of the list and if it returns True,
    the element is selected by the ft_filter() function.

    Needs two arguments : a str with no invisible or punctuation char
    and an integer
    usage -> python3 filterstring.py "words with space between" "6"
    """
    # print(main.__doc__)
    s = "the arguments are bad"
    try:
        assert len(sys.argv) == 3, s
        assert len(re.findall(r"[^\w\s]", sys.argv[1])) == 0, s
        assert len(re.findall(r"\d", sys.argv[2])) == len(sys.argv[2]), s
        S = sys.argv[1]
        N = int(sys.argv[2])
        filtered = ft_filter(string_filter, S.split())
        lambdaded = ft_filter(lambda x: len(x) > N, S.split())
        print(filtered)
        print(lambdaded)
    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
