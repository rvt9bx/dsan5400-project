import ssl                                                                                                     
import nltk
import os  
import textstat
from sentence_transformers import SentenceTransformer, util



def standardize_text(func):
    def wrapper(text):
        if not isinstance(text, str):
            return ""
        text =  ' '.join(text.split())
        result = func(text)
        return result
    return wrapper


class RecipeSummarizationEvaluator:
    """Evaluate simplified recipe text against the original text."""
    
    def __init__(self):
        # Fix SSL certificate issue and download cmudict for readability scoring
        ssl._create_default_https_context = ssl._create_unverified_context
        nltk_path = os.path.expanduser('~/nltk_data')
        os.makedirs(nltk_path, exist_ok=True)
        nltk.download('cmudict', download_dir=nltk_path, quiet=True)

        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def compute_semantic_similarity(self, modelresults):
        """
        Compute cosine similarity between the original and simplified texts.

        Uses the all-MiniLM-L6-v2 sentence transformer to generate embeddings,
        then computes cosine similarity. A score of 1.0 means identical meaning;
        lower scores indicate semantic drift.

        """
        original = modelresults['original']
        simplified = modelresults['simplified']

        original_std = standardize_text(original)
        simplified_std = standardize_text(simplified)

        embedding_original = self.model.encode(original_std, convert_to_tensor=True)
        embedding_simplified = self.model.encode(simplified_std, convert_to_tensor=True)

        similarity_score = util.cos_sim(embedding_original, embedding_simplified).item()

        return similarity_score
    
    def compute_compression_ratio(self, modelresults):
        """
        Compute the word-count ratio of simplified text to original text.

        A ratio below 1.0 means the simplified text is shorter. A ratio of 0.5
        means the simplified text is half the length of the original.

    
        """
        original = modelresults['original']
        simplified = modelresults['simplified']

        original_std = standardize_text(original)
        simplified_std = standardize_text(simplified)

        original_word_count = len(original_std.split())
        simplified_word_count = len(simplified_std.split())

        if original_word_count == 0:
            return 0.0

        return simplified_word_count / original_word_count
    
    def compute_readability(self, modelresults):
        """
        Compute Flesch-Kincaid Grade Level for both original and simplified texts.

        A lower grade level indicates easier readability. Comparing the two scores
        shows whether simplification reduced the reading difficulty.

        """
        original = modelresults['original']
        simplified = modelresults['simplified']

        original_std = standardize_text(original)
        simplified_std = standardize_text(simplified)

        readability_original = textstat.flesch_kincaid_grade(original_std)
        readability_simplified = textstat.flesch_kincaid_grade(simplified_std)

        return readability_original, readability_simplified
    

    def evaluate_simplification(self, pairs):
        """
        Run a full evaluation on a list of simplification pairs and print a summary report for each.

        Combines semantic similarity, compression ratio, and readability improvement
        into a single overall score. Prints a formatted report per recipe and returns
        a list of result dictionaries.

        Scoring rules:
            >= 0.80  Very Strong Simplification
            >= 0.65  Good
            >= 0.50  Moderate
            <  0.50  Weak

        Parameters
        ----------
        pairs : list of dict
            Each dict has keys 'original' and 'simplified', each containing a string of text.

        Returns
        -------
        list of dict
            One result dict per pair with keys: similarity, compression, readability_original,
            readability_simplified, readability_improvement, overall_score, rating.
        """
        results = []
        for i, pair in enumerate(pairs):
            print(f"\n--- Recipe {i + 1} ---")
            similarity = self.compute_semantic_similarity(pair)
            compression = self.compute_compression_ratio(pair)
            readability_original, readability_simplified = self.compute_readability(pair)

            readability_improvement = 1 - (readability_simplified / readability_original)
            overall_score = (similarity + compression + readability_improvement) / 3

            if overall_score >= 0.80:
                rating = "Very Strong Simplification"
            elif overall_score >= 0.65:
                rating = "Good"
            elif overall_score >= 0.50:
                rating = "Moderate"
            else:
                rating = "Weak"

            print("=" * 40)
            print("       SIMPLIFICATION EVALUATION")
            print("=" * 40)
            print(f"  Semantic Similarity:      {similarity:.4f}")
            print(f"  Compression Ratio:        {compression:.4f}")
            print(f"  Readability (Original):   {readability_original:.4f}")
            print(f"  Readability (Simplified): {readability_simplified:.4f}")
            print(f"  Readability Improvement:  {readability_improvement:.4f}")
            print("-" * 40)
            print(f"  Overall Score:            {overall_score:.4f}")
            print(f"  Rating:                   {rating}")
            print("=" * 40)

            results.append({
                "similarity": similarity,
                "compression": compression,
                "readability_original": readability_original,
                "readability_simplified": readability_simplified,
                "readability_improvement": readability_improvement,
                "overall_score": overall_score,
                "rating": rating
            })

        return results
    


if __name__ == "__main__":
    evaluator = RecipeSummarizationEvaluator()
    
    # # Example usage with dummy data
    # modelresults = {
    #     'original': "Preheat the oven to 350 degrees. Mix flour, sugar, and eggs. Bake for 30 minutes.",
    #     'simplified': "Set oven to 350°F. Combine flour, sugar, and eggs. Bake for 30 mins."
    # }
    
    # evaluation_results = evaluator.evaluate_simplification(modelresults)

        

