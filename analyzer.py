import spacy

nlp = spacy.load("en_core_web_sm")

word_frequencies = {
    "love": 500, "gratitude": 540, "joy": 540, "peace": 600,
    "fear": 100, "anger": 150, "guilt": 30, "shame": 20
}

def analyze_sentence(text):
    doc = nlp(text.lower())
    scores = [word_frequencies.get(token.text, 250) for token in doc if token.is_alpha]
    return {
        "average_score": sum(scores) / len(scores) if scores else 250,
        "token_scores": {token.text: word_frequencies.get(token.text, 250) for token in doc if token.is_alpha}
    }
