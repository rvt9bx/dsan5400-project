import csv
from summarizer import summarizer
import ast

# CSV Iterator Function
def iterator(in_path, out_path, ratio = 0.5):
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