from MultiExtractiveSummarizer import MultiExtractiveSummarizer
import re
import logging

logging = logging.getLogger(__name__)

# Model Function
_summarizer_model = None


def get_summarizer():
    """Return the singleton MultiExtractiveSummarizer instance, initializing it on first call.

    Returns:
        MultiExtractiveSummarizer: Loaded summarizer model using SBERT embeddings and KMeans clustering.
    """
    global _summarizer_model
    if _summarizer_model is None:
        _summarizer_model = MultiExtractiveSummarizer(embedding_method="sbert", summarization_method="kmeans")
    return _summarizer_model


# Summarizer Function
def summarizer(text, ratio=0.5):
    """Simplify recipe directions text using extractive summarization.

    Cleans the input text, then uses the MultiExtractiveSummarizer to select
    the most important sentences. Falls back to the original text if summarization fails.

    Args:
        text (str): Raw recipe directions text to simplify.
        ratio (float): Fraction of sentences to keep. Defaults to 0.5.

    Returns:
        str: Simplified directions text, or original text if summarization fails.
    """
    model = get_summarizer()

    clean_text = re.sub(r"[^\w\s/.]", "", text)
    clean_text = clean_text.replace("\u00b0", " degrees ")
    try:
        return model.summarize(clean_text, ratio=ratio)
    except Exception as e:
        print("Summarization failed, returning original text. See logs/simplifier.logs for traceback.")
        logging.error(f"Summarization failed: {e}")
        logging.info("Returning original text as fallback")
        return clean_text
