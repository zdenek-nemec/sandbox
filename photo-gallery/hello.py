def print_environment_info():
    import sys
    print(f"Python: {sys.version}")
    print(f"Environment: {sys.prefix}")


def main():
    print("Hello, World!")
    print_environment_info()


if __name__ == "__main__":
    main()
