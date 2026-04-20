import argparse

def load(filepath):
    """Loads data from filepath to the databse"""
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError:
        print(f"{filepath} not found")


def main():
    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards CLI",
        epilog="Enjoy and use witch cautious",
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "send"),
        default=help
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="The path to the file to load",
        default=help
    )
    args = parser.parse_args()
    try:
        globals()[args.subcommand](args.filepath)
    except KeyError:
        print("Subcommand is invalid")
 




if __name__ == "__main__":
    main()