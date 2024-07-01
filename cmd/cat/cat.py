import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='print the content of a file')
    parser.add_argument('-n', action='store_true',
                        help='number the output lines')
    parser.add_argument('filepath', default=None, help='read from a file')
    args = parser.parse_args()

    n = args.n
    filepath = args.filepath

    if filepath != None:
        with open(filepath, 'r') as f:
            reader = f.readlines()

    lineNumber = 1
    for line in reader:
        if n:
            print(f"{lineNumber}. {line.strip()}")
            lineNumber += 1
        else:
            print(line.strip())


if __name__ == "__main__":
    main()
