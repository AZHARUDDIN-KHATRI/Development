mport nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import collections

def nltk_summarizer(text: str, num_sentences: int = 2) -> str:
    """Extracts the top N sentences based on word frequency scoring."""
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    word_frequencies = collections.defaultdict(int)
    for word in words:
        if word.isalnum() and word not in stop_words:
            word_frequencies[word] += 1
    max_freq = max(word_frequencies.values()) if word_frequencies else 1
    for word in word_frequencies:
        word_frequencies[word] /= max_freq
    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return " ".join(summary_sentences)