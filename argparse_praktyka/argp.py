import argparse

parser = argparse.ArgumentParser(description="a random program that does something")


# parser.add_argument("filename", help=argparse.SUPPRESS)

# parser.add_argument("filename", help="filename of the file to process")
# parser.add_argument(
#     "-c", "--copy", dest="liczba_kopii", help="make n copies of the file", type=int
# )
# parser.add_argument("-s", "--something", action="store_true")
# parser.add_argument("-v", "--version", action="version", version="argp.py v1.0")
# parser.add_argument("-n", "--name", default="file_copy")

arguments = parser.parse_args()
print(arguments)
