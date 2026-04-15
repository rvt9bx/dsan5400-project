import csv
import random

# Set seed for reproducibility
random.seed(12)

# Train/Test Split
with open("summarizer/data/full_dataset.csv", "r", newline="") as input,\
        open("summarizer/data/train_dataset.csv", "w", newline="") as train_output,\
        open("summarizer/data/test_dataset.csv", "w", newline="") as test_output:
            
            reader = csv.reader(input)
            train_writer = csv.writer(train_output)
            test_writer = csv.writer(test_output)

            header = next(reader) # Skip header
            train_writer.writerow(header)
            test_writer.writerow(header)

            for row in reader:
                if random.random() < 0.8:
                    train_writer.writerow(row)
                else:
                    test_writer.writerow(row)

# Set New Seed
random.seed(32)

# Train/Validation Split
with open("summarizer/data/train_dataset.csv", "r", newline="") as input, \
     open("summarizer/data/train_split.csv", "w", newline="") as train_output, \
     open("summarizer/data/val_dataset.csv", "w", newline="") as val_output:

    reader = csv.reader(input)
    train_writer = csv.writer(train_output)
    val_writer = csv.writer(val_output)

    header = next(reader)
    train_writer.writerow(header)
    val_writer.writerow(header)

    for row in reader:
        if random.random() < 0.05:
            val_writer.writerow(row) 
        else:
            train_writer.writerow(row) 

# Set New Seed
random.seed(42)

# Subset Test Set
with open("summarizer/data/test_dataset.csv", "r", newline="") as input, \
     open("summarizer/data/test_split.csv", "w", newline="") as test_output, \
     open("summarizer/data/testsub_dataset.csv", "w", newline="") as sub_output:

    reader = csv.reader(input)
    test_writer = csv.writer(test_output)
    sub_writer = csv.writer(sub_output)

    header = next(reader)
    test_writer.writerow(header)
    sub_writer.writerow(header)

    for row in reader:
        if random.random() < 0.1:
            sub_writer.writerow(row) 
        else:
            test_writer.writerow(row) 