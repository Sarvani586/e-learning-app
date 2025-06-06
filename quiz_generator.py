import random
def generate_quiz(subject):
    # ✅ Normalize subject input (convert to lowercase for flexible matching)
    subject = subject.lower()

    # ✅ Predefined question sets for common subjects
    question_bank = {
        "python programming": [
            {"question": "What is Python mainly used for?", "options": ["A. Web Development", "B. Data Science", "C. Artificial Intelligence", "D. All of the above"], "answer": "D. All of the above"},
            {"question": "What keyword is used to define a function in Python?", "options": ["A. def", "B. func", "C. define", "D. function"], "answer": "A. def"},
            {"question": "Which data type is immutable in Python?", "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"], "answer": "C. Tuple"},
        ],
        "mathematics": [
            {"question": "What is the derivative of x^2?", "options": ["A. 2x", "B. x", "C. x^2", "D. None"], "answer": "A. 2x"},
            {"question": "What is the square root of 144?", "options": ["A. 10", "B. 12", "C. 14", "D. 16"], "answer": "B. 12"},
            {"question": "What is the value of π (pi) rounded to two decimal places?", "options": ["A. 3.12", "B. 3.14", "C. 3.16", "D. 3.18"], "answer": "B. 3.14"},
        ],
        "physics": [
            {"question": "What is Newton's First Law?", "options": ["A. F = ma", "B. Objects remain in motion or at rest unless acted upon by a force", "C. Every action has an equal and opposite reaction", "D. Energy is conserved"], "answer": "B. Objects remain in motion or at rest unless acted upon by a force"},
            {"question": "What unit is used to measure force?", "options": ["A. Joule", "B. Newton", "C. Pascal", "D. Watt"], "answer": "B. Newton"},
            {"question": "What is the speed of light?", "options": ["A. 300,000 km/s", "B. 150,000 km/s", "C. 500,000 km/s", "D. 100,000 km/s"], "answer": "A. 300,000 km/s"},
        ]
    }
    # ✅ Check if subject exists in predefined database
    if subject in question_bank:
        questions = question_bank[subject]
    else:
        # ✅ Dynamically generate questions for any subject entered
        questions = [
            {"question": f"What is a fundamental concept of {subject}?", "options": ["A. Structure", "B. Randomness", "C. Chaos", "D. Guesswork"], "answer": "A. Structure"},
            {"question": f"What is {subject} mainly used for?", "options": ["A. Learning", "B. Decoration", "C. Entertainment", "D. Nothing"], "answer": "A. Learning"},
            {"question": f"What is an essential tool in {subject}?", "options": ["A. Notebook", "B. Code", "C. Paintbrush", "D. Hammer"], "answer": "B. Code"},
            {"question": f"What skill improves {subject} expertise?", "options": ["A. Practice", "B. Guessing", "C. Sleeping", "D. None"], "answer": "A. Practice"},
            {"question": f"What is a key benefit of {subject}?", "options": ["A. Knowledge-building", "B. Time-wasting", "C. Confusion", "D. Distraction"], "answer": "A. Knowledge-building"},
        ]
    random.shuffle(questions)  # ✅ Randomize question order
    return questions
