import sys
import re

NESTED_MORSE = {'A': '.-', 'B': '-...',
                'C': '-.-.', 'D': '-..', 'E': '.',
                'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-',
                'L': '.-..', 'M': '--', 'N': '-.',
                'O': '---', 'P': '.--.', 'Q': '--.-',
                'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--',
                'X': '-..-', 'Y': '-.--', 'Z': '--..',
                '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.',
                '0': '-----', ' ': '/'}


def main():
    """
    this script will translate a string in alphanumeric char
    into morse code.
    usage = python3 sos.py "alphanumeric string"
    """
    # print(main.__doc__)
    e = "the arguments are bad"
    try:
        assert len(sys.argv) == 2, e
        assert len(re.findall(r"[^\w\s]", sys.argv[1])) == 0, e
        ret = ""
        s = sys.argv[1].upper()
        for c in range(0, len(s)):
            if s[c] in NESTED_MORSE:
                ret += NESTED_MORSE[s[c]]
                if (c < len(s) - 1):
                    ret += ' '
        print(ret)

    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
