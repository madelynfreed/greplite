import argparse
import walk

parser = argparse.ArgumentParser(description='toggling between AND and OR searching')
parser.add_argument('strings', metavar='S', type=str, nargs='+', help='strings for search')
parser.add_argument('-o', action=OrSearch)

