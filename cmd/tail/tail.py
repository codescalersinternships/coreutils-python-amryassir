import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description='print specific number of tail line')
    parser.add_argument('-n', type=int, default=10,
                        help='number of tail lines to print')
    parser.add_argument('filepath', nargs='?',
                        default=None, help='read from a file')
    args = parser.parse_args()

    n = args.n
    filepath = args.filepath

    if filepath != None:
        with open(filepath, 'r') as f:
            reader = f.readlines()
    else:
        reader = sys.stdin.readlines()

    for i in reader[-n:]:
        print(i.strip())


if __name__ == "__main__":
    main()
