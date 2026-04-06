# python bin/main.py -u recipe_url

# import packages 
import argparse
from recipe_simplifier.parser import parse_url

# add command line arguments
def parse_args():
    '''function to add command line arguments'''
    global args 
    parser = argparse.ArgumentParser(description="Simplifies Recipe Text")
    parser.add_argument("-u", "--url", required=True, help="recipe url")
    args = parser.parse_args()

# main function
def main():
    '''main function to run on command or when script is run'''
    parse_args()
    parse_url(args.url)

# main code 
if __name__ == "__main__":
    main()