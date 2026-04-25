import csv
from src.recipe_simplifier.summarizer import summarizer
import ast

# CSV Iterator Function
def iterator(in_path, out_path, ratio = 0.5):
    """Summarize recipe directions from a CSV and write original/simplified pairs to a new CSV.

    Args:
        in_path (str): Path to input CSV containing a 'directions' column.
        out_path (str): Path to write output CSV with 'original' and 'simplified' columns.
        ratio (float): Summarization ratio passed to the summarizer. Defaults to 0.5.

    Returns:
        None
    """
    with open(in_path, "r", newline="") as infile, \
     open(out_path, "w", newline="") as outfile:
        reader = csv.DictReader(infile)

        # Add a new dictionary for results
        writer = csv.DictWriter(outfile, fieldnames=["original", "simplified"])
        writer.writeheader()

        # Iterate through each row
        for row in reader:
            original = row["directions"]
            writer.writerow({"original": original,"simplified": summarizer(original, ratio = ratio)})

# CSV Processing Function
def process_file(input_path, output_path, scorer):
    """Apply a scoring function to each row in a CSV and write results to a new CSV.

    Args:
        input_path (str): Path to input CSV with 'original' and 'simplified' columns.
        output_path (str): Path to write output CSV with an added 'similarity' column.
        scorer (callable): Function that takes a row dict and returns a score.

    Returns:
        None
    """
    with open(input_path, "r", newline="") as infile, \
         open(output_path, "w", newline="") as outfile:
        reader = csv.DictReader(infile)

        # Add a new similarity value
        fieldnames = reader.fieldnames + ["similarity"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate through each row
        for row in reader:
            similarity = scorer(row)
            row["similarity"] = similarity
            writer.writerow(row)

# Mean Function
def mean(file_path):
    """Compute the mean of the 'similarity' column in a scored CSV file.

    Args:
        file_path (str): Path to CSV containing a 'similarity' column of floats.

    Returns:
        float: Mean similarity score, or 0 if the file is empty.
    """
    total = 0
    count = 0
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["similarity"])
            count += 1

    return total / count if count else 0

# Comparison Function
def comparison(file_path):
    """Compare readability scores between original and simplified recipes in a CSV.

    Prints counts and ratio of recipes where simplification improved readability.

    Args:
        file_path (str): Path to CSV where 'similarity' column contains (original, simplified) tuples.

    Returns:
        float: Ratio of more-readable to less-readable simplified recipes.
    """
    more_readable = 0
    less_readable = 0
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            tup = ast.literal_eval(row["similarity"])
            original, simple = map(float, tup)
            if original >= simple:
                more_readable +=1
            else:
                less_readable +=1
    print("More Readable Recipes: " + str(more_readable))
    print("Less Readable Recipes: " + str(less_readable))
    print("Ratio of More to Less: " + str(more_readable/less_readable))
    ratio = more_readable/less_readable
    return ratio