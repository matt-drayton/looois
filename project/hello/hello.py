#!/bin/python3
"""
Print a friendly statement to the console.
"""

import argparse


def hello(s="world"):
    """Generate a string that greets the subject (i.e. "Hello, world!").

    Args:
        s (str, optional): The subject of the greeting. Defaults to "world".

    Returns:
        str: A friendly message to greet the subject.
    """
    message = "Hello, " + s + "!"
    return message


def main(word):
    """Print a friendly greeting to the user's command line.

    Args:
        word (str): The subject of the greeting.
    """
    output = hello(word)
    print(output)


if __name__ == "__main__":
    """Run the module as a script."""

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "word",
        help="customise the subject of the output message",
        nargs="?",
        default="world",
        type=str,
    )
    args = parser.parse_args()

    # Call main function
    main(args.word)
