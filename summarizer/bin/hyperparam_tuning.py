from summarizer.utils import iterator, process_file, mean, comparison
from summarizer.eval import RecipeSummarizationEvaluator

# Create eval object
evaluator = RecipeSummarizationEvaluator()

# Define hyperparameters
ratios = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

for ratio in ratios:
    # Perform summarization/write to new file
    iterator("summarizer/data/val_dataset.csv", "summarizer/data/summaries.csv", ratio = ratio)

    print("Ratio: " + str(ratio))

    # Perform Cosine Similarity
    process_file("summarizer/data/summaries.csv", "summarizer/data/scores.csv", evaluator.compute_semantic_similarity)
    final_score = mean("summarizer/data/scores.csv")
    print(final_score)

    # Perform Compression Ratio
    process_file("summarizer/data/summaries.csv", "summarizer/data/scores.csv", evaluator.compute_compression_ratio)
    final_score = mean("summarizer/data/scores.csv")
    print(final_score)

    # Perform Readability Score
    process_file("summarizer/data/summaries.csv", "summarizer/data/scores.csv", evaluator.compute_readability)
    comparison("summarizer/data/scores.csv")

