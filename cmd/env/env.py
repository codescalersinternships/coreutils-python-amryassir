import os


def main():
    envs = os.environ
    for key, value in envs.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
