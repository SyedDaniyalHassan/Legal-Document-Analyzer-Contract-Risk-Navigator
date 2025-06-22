import streamlit as st
st.set_page_config(page_title="Legal Document Analyzer & Contract Risk Navigator")
from graph import get_graph_executor
from vector_store import build_vector_store, semantic_search
from report_generator import generate_report
from state_schema import State

def parse_file(uploaded_file):
    import pypdf
    from docx import Document
    if uploaded_file.name.endswith(".pdf"):
        reader = pypdf.PdfReader(uploaded_file)
        return "\n".join(page.extract_text() for page in reader.pages)
    elif uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join([p.text for p in doc.paragraphs])
    return ""

st.title("Legal Document Analyzer")
uploaded_file = st.file_uploader("Upload contract (PDF or DOCX)", type=["pdf", "docx"])
if uploaded_file:
    text = parse_file(uploaded_file)
    state = State(text=text)
    executor = get_graph_executor()
    with st.spinner("Analyzing document. This may take a minute..."):
        result = executor.invoke(state)
    st.subheader("Clause Analysis")
    for clause, data in result["clauses"].items():
        clause_text = data["text"] if isinstance(data, dict) and "text" in data else data
        if clause_text and clause_text.strip() and clause_text.strip().upper() != "MISSING":
            st.markdown(f"**{clause}**")
            st.text_area("Clause Text", clause_text, height=80, key=clause)
            if isinstance(data, dict) and "risk" in data:
                st.write(f"Risk: {data['risk']}")
            if isinstance(data, dict) and "comments" in data:
                st.write(f"Comments: {data['comments']}")
            new_risk = st.selectbox("Override Risk?", ["", "low", "medium", "high"], key=f"{clause}_risk")
            if new_risk and isinstance(data, dict):
                result["clauses"][clause]["risk"] = new_risk
    st.write(f"**Overall Risk:** {result['overall_risk']}")
    st.download_button("Download JSON Report", result["json_report"], file_name="report.json")
    st.download_button("Download PDF Report", result["pdf_report"].getvalue(), file_name="report.pdf")
    # st.subheader("Ask a question about the contract")
    # question = st.text_input("Your question")
    # if question:
    #     with st.spinner("Searching for answer..."):
    #         db = build_vector_store([text])
    #         answer = semantic_search(db, question)
    #     st.write("Relevant section(s):")
    #     for doc in answer:
    #         st.write(doc.page_content) 