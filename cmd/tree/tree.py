import argparse
import os


def print_dir(dir_path, depth, current_depth=0):
    if current_depth > depth:
        return

    try:
        entries = os.listdir(dir_path)
    except OSError as e:
        print(f"Error reading directory {dir_path}: {e}")
        return

    for entry in entries:
        prefix = "|"
        indent = "――"
        if current_depth > 0:
            prefix = "|" + "    " * current_depth
            indent = prefix + "――"
        print(prefix)
        print(indent, entry)

        entry_path = os.path.join(dir_path, entry)
        if os.path.isdir(entry_path) and current_depth < depth:
            print_dir(entry_path, depth, current_depth + 1)


def main():
    parser = argparse.ArgumentParser(
        description='Print directory structure up to a specified depth.')
    parser.add_argument('directory', type=str, help='Directory path to print')
    parser.add_argument('-depth', type=int, default=1, help='Depth to print')

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory.")
        return

    print_dir(args.directory, args.depth)


if __name__ == '__main__':
    main()
