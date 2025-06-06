import streamlit as st
import random
from content_generator import generate_lesson
from quiz_generator import generate_quiz
from score_evaluator import evaluate_score
from summarizer import generate_summary

# ✅ Add Background Image
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20190220/ourmid/pngtree-blue-business-technology-user-image_6481.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)  # ✅ Set Background

# ✅ App Title
st.title("E-Learning Quiz & Summary App")
st.write("Welcome to the interactive learning platform!")  # ✅ Introductory text

# ✅ User Input for Subject
subject = st.text_input("Enter a topic:")

if subject:  # ✅ Ensure the user enters a topic first
    # ✅ Ask User Whether to Conduct Quiz or Generate Summary
    action = st.radio(
        f"What would you like to do with '{subject}'?",
        ["Generate a Summary", "Conduct a Quiz"],
        key="user_action"
    )

    if action == "Generate a Summary":
        st.subheader(f"Lesson Summary on {subject}")
        st.write(generate_lesson(subject))
        st.subheader(f"Summary of {subject}")
        st.write(generate_summary(subject))

    elif action == "Conduct a Quiz":
        st.subheader(f"Quiz on {subject}")
        questions = generate_quiz(subject)
        score = 0  # ✅ Initialize Score

        # ✅ Display Questions & Capture User Input
        for q in questions:
            selected_option = st.radio(q["question"], q["options"], key=q["question"])
            if selected_option == q["answer"]:
                st.success("✅ Correct!")
                score += 20  # ✅ Each question carries 20 points
            else:
                st.error("❌ Incorrect!")

        # ✅ Display Final Score & Evaluation
        st.subheader(f"Your Score: {score} / 100")
        st.write(evaluate_score(score))

        # ✅ Final "THANK YOU" Message
        st.success("🎉 THANK YOU for participating in the quiz! Keep learning and growing! 🚀")
