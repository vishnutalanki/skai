import streamlit as st
import tempfile
from ai_engine import generatePlan

from PyPDF2 import PdfReader
from docx import Document



st.set_page_config(page_title="SKAI Co-Design Agent", layout="centered")
st.title("🧠 SKAI Co-Design Agent")
st.caption("Upload or paste materials + generate instructional guidance powered by GPT-4o.")

# ----------- INPUT SECTION ------------------
st.markdown("### 📄 Step 1: Upload or Paste Your Unit Content")

uploaded_file = st.file_uploader("Upload lesson/unit file (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])
unit_input = st.text_area("...or paste the lesson/unit text here", height=200)

extracted_text = ""

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(tmp_path)
        extracted_text = "\n".join([page.extract_text() or "" for page in reader.pages])
    elif uploaded_file.name.endswith(".docx"):
        doc = Document(tmp_path)
        extracted_text = "\n".join([para.text for para in doc.paragraphs])
    elif uploaded_file.name.endswith(".txt"):
        with open(tmp_path, "r") as f:
            extracted_text = f.read()

combined_input = unit_input.strip() + "\n" + extracted_text.strip()

# ----------- CUSTOMIZATION SECTION ------------------
st.markdown("### 🧭 Step 2: Add Optional Design Instructions")
with st.expander("Customize Your Request", expanded=False):
    theme = st.text_input("Theme or Focus (e.g., identity, poetry, SEL)")
    desired_standard = st.text_input("Targeted Standards (e.g., RL.6.1, L.6.5)")
    tone = st.selectbox("Output Tone", ["Professional", "Conversational", "Creative"], index=1)

# ----------- AI CALL ------------------
if st.button("✨ Generate Suggestions"):
    if not combined_input.strip():
        st.warning("Please provide content via upload or paste.")
    else:
        with st.spinner("Thinking deeply about your content..."):
            response = generatePlan(
                combined_input=combined_input,
                theme=theme,
                desired_standard=desired_standard,
                tone=tone
            )
            result = response

        st.markdown("---")
        st.markdown("## ✨ AI-Generated Co-Design Suggestions")
        st.markdown(result)
        st.success("Your custom instructional plan is ready!")



# openai.chat.completions.create(
#                 model="gpt-4o",
#                 messages=[
#                     {"role": "system", "content": "You're a top-tier instructional designer for middle school ELA."},
#                     {"role": "user", "content": prompt_build.strip()}
#                 ]
#             )
#             result = response.choices[0].message.content