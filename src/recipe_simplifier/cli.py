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
    args = parser.parse_args()

# main function
def main():
    '''main function to run on command or when script is run'''
    parse_args()

    # get original recipe 
    original_recipe = parse_url(args.url)

    # run summarizer 
    instructions_string = "\n".join(original_recipe.instructions)
    summarized_instructions = summarizer(instructions_string)
    print(summarized_instructions)
    # summarized_recipe = Recipe(original_recipe.title, original_recipe.ingredients, summarized_instructions)
    # # print or display 
    # summarized_recipe.print()
    # eval 

# main code 
if __name__ == "__main__":
    main()