import streamlit as st
import textstat
import re
from typing import Dict
st.set_page_config(page_title="Contract Simplifier — Prototype", layout="wide")
st.title("📄 Contract Language Simplifier — Prototype")

SAMPLE_TEXTS = {
    "Example 1 — Short": "The party of the first part shall, notwithstanding anything herein, terminate the agreement if obligations are not met.",
    "Example 2 — Medium": "Pursuant to the terms herein, the aforementioned supplier shall commence delivery within thirty (30) days and shall not be liable for delays beyond its control.",
    "Example 3 — Long": "Notwithstanding the provisions of Section 4, if the party fails to comply with the obligations, the contract may be terminated and the indemnifying party shall be responsible for any and all damages incurred." 
}

st.sidebar.header("Sample texts")
choice = st.sidebar.selectbox("Choose sample", ["(none)"] + list(SAMPLE_TEXTS.keys()))

if choice != "(none)":
    user_input = st.text_area("Enter Contract Text", value=SAMPLE_TEXTS[choice], height=250)
else:
    user_input = st.text_area("Enter Contract Text", height=250)

st.sidebar.markdown("---")
if st.sidebar.button("Clear input"):
    user_input = ""

REPLACEMENTS: Dict[str, str] = {
    "hereinafter": "from now on",
    "aforementioned": "mentioned earlier",
    "pursuant to": "under",
    "in accordance with": "according to",
    "notwithstanding": "despite",
    "shall": "must",
    "terminate": "end",
    "commence": "start",
    "indemnifying": "responsible",
    "obligations": "requirements",
}

def simplify_text(text: str) -> str:
    if not text:
        return ""
    simplified = text
    # Replace multi-word phrases first (longer keys first)
    for key in sorted(REPLACEMENTS.keys(), key=lambda k: -len(k)):
        simplified = re.sub(rf"\\b{re.escape(key)}\\b", REPLACEMENTS[key], simplified, flags=re.IGNORECASE)
    # Collapse multiple spaces
    simplified = re.sub(r"\\s+", " ", simplified).strip()
    return simplified

def summarize_text(text: str) -> str:
    if not text:
        return ""
    sentences = re.split(r'(?<=[.!?])\\s+', text.strip())
    return " ".join(sentences[:2])

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Original")
    st.write(user_input or "—")

with col2:
    st.subheader("Actions")
    if st.button("Simplify"):
        simplified = simplify_text(user_input)
        summary = summarize_text(simplified or user_input)
        st.session_state['simplified'] = simplified
        st.session_state['summary'] = summary
    if st.button("Summarize only"):
        st.session_state['summary'] = summarize_text(user_input)

simplified = st.session_state.get('simplified', '')
summary = st.session_state.get('summary', '')

st.subheader("Simplified Text")
if simplified:
    st.write(simplified)
    score = textstat.flesch_reading_ease(simplified)
    st.metric("Flesch Reading Ease", f"{score:.1f}")
    st.download_button("Download simplified text", simplified, file_name="simplified.txt")
else:
    st.info("Click 'Simplify' to generate a simplified version.")

st.subheader("Summary")
if summary:
    st.info(summary)
else:
    st.write("—")

st.sidebar.markdown("---")
st.sidebar.write("Prototype: lightweight simplifier + summary + readability score")

st.markdown("---")
st.caption("This is a minimal, self-contained prototype. For production, connect models, DB, and secrets.")
<<<<<<< HEAD
import streamlit as st
import textstat
import re

st.set_page_config(page_title="Contract Simplifier", layout="wide")
st.title("📄 Contract Language Simplifier")

import streamlit as st
import textstat
import re
from typing import Dict


st.set_page_config(page_title="Contract Language Simplifier", layout="wide")

st.title("📄 Contract Language Simplifier")


REPLACEMENTS: Dict[str, str] = {
    "hereinafter": "from now on",
    "aforementioned": "mentioned earlier",
    "pursuant to": "under",
    "in accordance with": "according to",
    "notwithstanding": "despite",
    "shall": "must",
    "terminate": "end",
    "commence": "start",
    "indemnifying": "responsible",
    "obligations": "requirements",
}


def simplify_text(text: str) -> str:
    if not text:
        return ""
    simplified = text
    for key in sorted(REPLACEMENTS.keys(), key=lambda k: -len(k)):
        simplified = re.sub(rf"\\b{re.escape(key)}\\b", REPLACEMENTS[key], simplified, flags=re.IGNORECASE)
    simplified = re.sub(r"\\s+", " ", simplified).strip()
    return simplified


def summarize_text(text: str) -> str:
    if not text:
        return ""
    sentences = re.split(r'(?<=[.!?])\\s+', text.strip())
    return " ".join(sentences[:2])


def main() -> None:
    st.subheader("Input")
    user_input = st.text_area("Enter Contract Text", height=250)

    col1, col2 = st.columns([2, 1])
    with col2:
        st.subheader("Actions")
        if st.button("Simplify"):
            if not user_input.strip():
                st.warning("Enter text first")
            else:
                st.session_state['simplified'] = simplify_text(user_input)
                st.session_state['summary'] = summarize_text(user_input)
        if st.button("Summarize only"):
            st.session_state['summary'] = summarize_text(user_input)

    simplified = st.session_state.get('simplified', '')
    summary = st.session_state.get('summary', '')

    st.subheader("Simplified Text")
    if simplified:
        st.write(simplified)
        st.download_button("Download simplified text", simplified, file_name="simplified.txt")
        score = textstat.flesch_reading_ease(simplified)
        st.metric("Flesch Reading Ease", f"{score:.1f}")
    else:
        st.info("Click 'Simplify' to generate a simplified version.")

    st.subheader("Summary")
    if summary:
        st.info(summary)
    else:
        st.write("—")


if __name__ == "__main__":
    main()
        with col2:
            st.subheader("Simplified")
            st.write(simplified)

        st.subheader("Summary")
        st.info(summary)

        score = textstat.flesch_reading_ease(simplified)
        st.subheader("Readability Score")
<<<<<<< HEAD
        st.write(score)
=======
        st.write(score)


if __name__ == "__main__":
    main()
>>>>>>> 29dfa08 (Use Streamlit in render.yaml; fix Streamlit app (app.py))
=======
>>>>>>> 552acaf (Add prototype and update app.py and render config)
