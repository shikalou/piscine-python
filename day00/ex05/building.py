import sys
import re


def main():
    """
    this script takes a string as only parameter,
    count each type of char in the string and returns the results
    """
    # print(main.__doc__)
    s = ""
    try:
        if (len(sys.argv) == 1):
            print("What is the text to count?")
            for line in sys.stdin:
                s += line
        else:
            assert len(sys.argv) <= 2, "more than one argument is provided"
            s = sys.argv[1]
        print("The text contains", len(s), "characters:")
        print(len(re.findall(r'[A-Z]', s)), "upper letters")
        print(len(re.findall(r'[a-z]', s)), "lower letters")
        print(len(re.findall(r"[^a-zA-Z0-9\s]", s)), "punctuation marks")
        print(sum([1 for i in s if i.isspace()]), "spaces")
        print(len(re.findall(r'\d', s)), "digits")

    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
