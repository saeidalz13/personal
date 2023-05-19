import argparse


def main():
    parser = argparse.ArgumentParser(description="saeid personal library")
    parser.add_argument(
        "command",
        help="Command to execute",
    )
    args = parser.parse_args()

    if args.command == "add_td":
        from saeid.TD import add_td

        add_td.main()

    elif args.command == "show_td":
        from saeid.TD import show_td

        show_td.main()
    else:
        raise TypeError("Wrong command")


if __name__ == "__main__":
    main()
