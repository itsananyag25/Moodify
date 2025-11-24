def detect_mood(text):
    text_lower = text.lower()
    if any(word in text_lower for word in ["happy", "excited", "joy"]):
        return "happy"
    elif any(word in text_lower for word in ["romantic","lofi","love"]):
        return "romantic"
    elif any(word in text_lower for word in ["sad", "down", "cry"]):
        return "sad"
    elif any(word in text_lower for word in ["angry", "mad", "furious"]):
        return "angry"
    elif any(word in text_lower for word in ["calm", "relaxed", "peaceful"]):
        return "calm"
    else:
        import random
        words = ["hits", "top songs", "viral", "trending", "mix","bollywood"]
        random_genre = random.choice(words)
        return random_genre