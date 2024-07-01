import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description='count lines, words, and characters')
    parser.add_argument('-l', action='store_true', help='get number of lines')
    parser.add_argument('-w', action='store_true', help='get number of words')
    parser.add_argument('-c', action='store_true',
                        help='get number of characters')
    parser.add_argument('filepath', nargs='?',
                        default=None, help='read from a file')
    args = parser.parse_args()

    filepath = args.filepath
    l = args.l
    w = args.w
    c = args.c

    if filepath != None:
        with open(filepath, 'r') as f:
            reader = f.readlines()
    else:
        reader = sys.stdin.readlines()

    lines, words, chars = 0, 0, 0

    for line in reader:
        lines += 1
        chars += len(line)
        word = line.split()
        words += len(word)

    check = not l and not w and not c

    if check or l:
        print(lines)
    if check or w:
        print(words)
    if check or c:
        print(chars)


if __name__ == "__main__":
    main()
