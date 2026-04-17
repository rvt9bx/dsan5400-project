# hide / log warnings
import sys
import os

os.makedirs("logs", exist_ok=True)
_log_file = open("logs/simplifier.log", "w")
sys.stderr = _log_file
os.environ["HF_HUB_DISABLE_IMPLICIT_TOKEN"] = "1"

import logging
logging.basicConfig(
    level=logging.WARNING,
    stream=_log_file,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

# import rest of packages
import argparse
from recipe_simplifier.parser import parse_url
from recipe_simplifier.recipe import Recipe
from recipe_simplifier.summarizer import summarizer
from recipe_simplifier.eval import eval

# add command line arguments
def parse_args():
    '''function to add command line arguments'''
    global args 
    parser = argparse.ArgumentParser(description="Simplifies Recipe Text")
    parser.add_argument("-u", "--url", required=True, help="recipe url")
    parser.add_argument("-p", "--print", action="store_true", help="print results to terminal")
    parser.add_argument("-d", "--display", action="store_true", help="open browser to display results as html")
    parser.add_argument("-s", "--save", required=False, help="file path to save html")
    parser.add_argument("-e", "--evaluate", action="store_true", help="evaluate the summarization")
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

    # print or display / save 
    if args.print:
        summarized_recipe.print()
    if args.display:
        summarized_recipe.display(args.save)

    # eval 
    if args.evaluate:
        evaluator = eval.RecipeSummarizationEvaluator()
        modelresults = {'original': original_recipe.instructions,
                        'simplified': summarized_recipe.instructions
                        }

        evaluator.evaluate_simplification([modelresults])

# main code 
if __name__ == "__main__":
    main()