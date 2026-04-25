import sys
import os
import logging
import argparse

# log warnings from model imports
os.makedirs("logs", exist_ok=True)
_log_file = open("logs/simplifier.log", "w")
sys.stderr = _log_file
os.environ["HF_HUB_DISABLE_IMPLICIT_TOKEN"] = "1"
logging.basicConfig(
    level=logging.INFO,
    stream=_log_file,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

# import rest of packages
from recipe_simplifier.parser import parse_url
from recipe_simplifier.recipe import Recipe
from recipe_simplifier.summarizer import summarizer
from recipe_simplifier.eval import eval


# add command line arguments
def parse_args():
    """Parse and store command line arguments for the recipe simplifier CLI.

    Returns:
        None: Arguments are stored in the global `args` variable.
    """
    global args
    parser = argparse.ArgumentParser(description="Simplifies Recipe Text")
    parser.add_argument("-u", "--url", required=True, help="recipe url")
    parser.add_argument("-og", "--original", action="store_true", help="print/display original recipe, not summarization")
    parser.add_argument("-p", "--print", action="store_true", help="print results to terminal")
    parser.add_argument("-d", "--display", action="store_true", help="open browser to display results as html")
    parser.add_argument("-s", "--save", required=False, help="file path to save html")
    parser.add_argument("-e", "--evaluate", action="store_true", help="evaluate the summarization")
    args = parser.parse_args()


# main function
def main():
    """Run the recipe simplifier pipeline from CLI arguments.

    Parses a recipe URL, optionally summarizes the directions, and prints,
    displays, or evaluates the result based on the provided flags.

    Returns:
        None
    """
    parse_args()

    # get original recipe
    original_recipe = parse_url(args.url)
    logging.info("Parsed recipe: '%s' from %s", original_recipe.title, args.url)

    # run summarizer
    if args.original:
        recipe = original_recipe
        logging.info("Using original recipe (no summarization)")
    else:
        logging.info("Running summarizer...")
        summarized_instructions = summarizer(original_recipe.instructions)
        logging.info("Summarization complete")
        recipe = Recipe(original_recipe.title, original_recipe.ingredients, summarized_instructions)

    # print or display / save
    if args.print:
        recipe.print()
    if args.display:
        recipe.display(args.save)

    # eval
    if args.evaluate:
        if args.original:
            logging.error("--evaluate cannot be used with --original")
            raise ValueError("--evaluate requires a summarized recipe; remove --original")
        else:
            logging.info("Running evaluation...")
            try:
                evaluator = eval.RecipeSummarizationEvaluator()
                modelresults = {"original": original_recipe.instructions, "simplified": recipe.instructions}

                evaluator.evaluate_simplification([modelresults])
                logging.info("Evaluation complete")
            except Exception as e:
                print("Evaluation failed, see logs/simplifier.logs for traceback.")
                logging.error(f"Evaluation failed: {e}")


# main code
if __name__ == "__main__":
    main()
