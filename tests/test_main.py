import pytest
from src.recipe_simplifier.eval import RecipeSummarizationEvaluator
from scripts.iterator import iterator, process_file, mean, comparison

# Text Preparation
iterator("tests/data/test_data.csv", "tests/data/summaries.csv")

# Initalize Class
evaluator = RecipeSummarizationEvaluator()

# Test Cosine Simlarity
def test_cosine():
    process_file("tests/data/summaries.csv", "tests/data/scores.csv", evaluator.compute_semantic_similarity)
    final_score = mean("tests/data/scores.csv")
    assert 0.5 < final_score < 1

# Test Compression Score
def test_compression():
    process_file("tests/data/summaries.csv", "tests/data/scores.csv", evaluator.compute_compression_ratio)
    final_score = mean("tests/data/scores.csv")
    assert 0.3 < final_score < 0.7

# Test Readability Score
def test_readability():
    process_file("tests/data/summaries.csv", "tests/data/scores.csv", evaluator.compute_readability)
    final_score = comparison("tests/data/scores.csv")
    assert 0 < final_score 