# python bin/main.py -u recipe_url

# import packages 
import argparse
from recipe_simplifier.parser import parse_url

# add command line arguments
def parse_args():
    global args 
    parser = argparse.ArgumentParser(description="Simplifies Recipe Text")
    parser.add_argument("-u", "--url", required=True, help="recipe url")
    args = parser.parse_args()

# main function
def main():
    parse_args()
    print(args.url)
    parse_url()

# main code 
if __name__ == "__main__":
    main()