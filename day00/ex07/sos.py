import sys

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
        assert all(c in NESTED_MORSE for c in sys.argv[1].upper()), e
        s = sys.argv[1].upper()
        print(" ".join([NESTED_MORSE[c] for c in s if c in NESTED_MORSE]))
    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
