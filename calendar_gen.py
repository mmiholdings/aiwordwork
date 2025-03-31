import random

hfw_words = [
    "Love", "Gratitude", "Joy", "Peace", "Abundance", "Harmony",
    "Compassion", "Empowerment", "Appreciation", "Serenity"
]

def generate_hfw_calendar(user_info):
    calendar = {}
    random.shuffle(hfw_words)
    for i in range(31):
        word = hfw_words[i % len(hfw_words)]
        calendar[f"Day {i+1}"] = {
            "word": word,
            "affirmation": f"I embody {word.lower()} today.",
            "frequency": 528,
            "chakra": "Heart"
        }
    return calendar
