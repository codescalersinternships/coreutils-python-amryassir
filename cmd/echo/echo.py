import argparse


def main():
    parser = argparse.ArgumentParser(description='echo the input test')
    parser.add_argument('-n', action='store_true',
                        help='omits the trailing newline.')
    parser.add_argument('input', nargs=argparse.REMAINDER,
                        help='input to print')
    args = parser.parse_args()

    n = args.n
    out = ' '.join(args.input)

    if n:
        print(out, end='')
    else:
        print(out)


if __name__ == "__main__":
    main()
