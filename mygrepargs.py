import argparse
import walk

parser = argparse.ArgumentParser(description='toggling between AND and OR searching')
parser.add_argument('strings', metavar='S', nargs='+', help='strings for search')
parser.add_argument('-o', action='store_true', help='search with OR instead of the default AND')


