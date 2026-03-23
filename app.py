import streamlit as st
import textstat
import re

st.set_page_config(page_title="Contract Simplifier", layout="wide")

st.title("📄 Contract Language Simplifier")

def simplify_text(text):
    replacements = {
        "hereinafter": "from now on",
        "aforementioned": "mentioned earlier",
        "pursuant to": "under",
        "in accordance with": "according to",
        "notwithstanding": "despite",
        "shall": "must",
        "terminate": "end",
        "commence": "start",
    }

    for word, simple in replacements.items():
        text = re.sub(rf"\b{word}\b", simple, text, flags=re.IGNORECASE)

    return text


def summarize_text(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    return " ".join(sentences[:2])


user_input = st.text_area("Enter Contract Text", height=250)

if st.button("Simplify"):

    if not user_input.strip():
        st.warning("Enter text first")
    else:
        simplified = simplify_text(user_input)
        summary = summarize_text(user_input)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original")
            st.write(user_input)

        with col2:
            st.subheader("Simplified")
            st.write(simplified)

        st.subheader("Summary")
        st.info(summary)

        score = textstat.flesch_reading_ease(simplified)

        st.subheader("Readability Score")
        st.write(score)
