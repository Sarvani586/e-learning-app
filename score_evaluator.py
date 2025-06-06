def evaluate_score(score):
    if 80 <= score <= 100:
        return "🌟 Very Good! You have an excellent understanding."
    elif 50 <= score < 80:
        return "👍 Good job! You have a solid grasp of the topic."
    elif 30 <= score < 50:
        return "📚 Average! Keep reviewing the content."
    else:
        return "📝 Practice more and come back!"
