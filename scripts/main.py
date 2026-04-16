from iterator import iterator, process_file, mean, comparison
from recipe_simplifier.eval.eval import RecipeSummarizationEvaluator

# Create eval object
evaluator = RecipeSummarizationEvaluator()

# Perform summarization/write to new file
iterator("../data/testsub_dataset.csv", "../data/summaries.csv")

# Perform Cosine Similarity
process_file("../data/summaries.csv", "../data/scores.csv", evaluator.compute_semantic_similarity)
final_score = mean("../data/scores.csv")
print(final_score)

# Perform Compression Ratio
process_file("../data/summaries.csv", "../data/scores.csv", evaluator.compute_compression_ratio)
final_score = mean("../data/scores.csv")
print(final_score)

# Perform Readability Score
process_file("../data/summaries.csv", "../data/scores.csv", evaluator.compute_readability)
comparison("../data/scores.csv")