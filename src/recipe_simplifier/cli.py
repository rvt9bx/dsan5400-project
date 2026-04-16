import argparse
from recipe_simplifier.parser import parse_url
from recipe_simplifier.recipe import Recipe
from recipe_simplifier.summarizer import summarizer

# add command line arguments
def parse_args():
    '''function to add command line arguments'''
    global args 
    parser = argparse.ArgumentParser(description="Simplifies Recipe Text")
    parser.add_argument("-u", "--url", required=True, help="recipe url")
    parser.add_argument("-p", "--print", action="store_true", help="print results to terminal")
    parser.add_argument("-d", "--display", action="store_true", help="open browser to display results as html")
    args = parser.parse_args()

# main function
def main():
    '''main function to run on command or when script is run'''
    parse_args()

    # get original recipe 
    original_recipe = parse_url(args.url)

    # run summarizer 
    summarized_instructions = summarizer(original_recipe.instructions)
    summarized_recipe = Recipe(original_recipe.title, original_recipe.ingredients, summarized_instructions)

    # print or display 
    if args.print:
        summarized_recipe.print()
    if args.display:
        summarized_recipe.display()

    # eval 

# main code 
if __name__ == "__main__":
    main()