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
