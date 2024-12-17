import argparse

def arg_parser():
    parser = argparse.ArgumentParser(
        description="Perform search using Linear or Binary Search with different approaches."
    )

    parser.add_argument(
        "arr",
        type=str,
        nargs="?",
        default="10,23,45,70,11,15",
        help="Comma-separated list of numbers (e.g., 10,23,45,70,11,15)"
    )
    parser.add_argument(
        "target", type=int, nargs="?", default=70, help="Target value to search in the list"
    )
    parser.add_argument(
        "-alg", "--algorithm",
        choices=["linear", "binary"],
        default="linear",
        help="The algorithm to perform the search: 'linear' or 'binary'"
    )
    parser.add_argument(
        "-ap", "--approach",
        choices=["iterative", "recursive", "regex"],
        default="iterative",
        help="The approach to perform the search"
    )

    return parser.parse_args()