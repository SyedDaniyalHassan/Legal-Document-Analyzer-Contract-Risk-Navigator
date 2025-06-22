# Legal Document Analyzer & Contract Risk Navigator

## Description

**Legal Document Analyzer & Contract Risk Navigator** is an AI-powered web application that streamlines the review and risk assessment of legal contracts. Upload your legal documents (PDF or DOCX), and the system will:

- Automatically extract key clauses (Termination, Payment, NDA, Indemnity, Data Privacy, etc.) using advanced LLMs.
- Assess the risk level of each clause (low, medium, high, or missing/partial) with detailed, context-aware analysis.
- Generate a structured, downloadable report (JSON/PDF) summarizing findings and risks.
- Allow users to ask natural language questions about the contract and receive relevant answers.
- Provide a user-friendly interface with real-time feedback and human-in-the-loop risk override options.

The solution leverages LangChain, LangGraph, Together AI, and modern NLP techniques to deliver robust, explainable, and efficient contract analysis for legal professionals, businesses, and compliance teams.

---

## Features

- **Document Upload:** Supports PDF and DOCX contract files.
- **Clause Extraction:** Identifies and extracts important clauses, even if not explicitly labeled.
- **Risk Analysis:** Classifies each clause as low, medium, high, or missing/partial risk, with detailed comments.
- **Interactive UI:** Review, override, and download results. Ask questions about the contract.
- **Report Generation:** Download structured JSON and PDF reports.
- **Modern LLM Integration:** Uses Together AI and Llama-3 for robust clause extraction and analysis.

---

## Setup & Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd LegalSaaS
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # Or
   source .venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Get your API Token:**

   - **For Together AI (Recommended for Llama-3, Gemma, etc.):**
     1. Sign up at [Together AI](https://www.together.ai/)
     2. Go to your [API Keys page](https://app.together.ai/settings/apikeys)
     3. Click "Create API Key" and copy the generated key.
     4. Add it to your `.env` file in your project root:
        ```env
        HUGGINGFACEHUB_API_TOKEN=your_together_api_key_here
        ```
---

5. **Run the app:**
   ```sh
   streamlit run app.py
   ```

6. **Open your browser:**
   - Go to [http://localhost:8501](http://localhost:8501)

---

## Usage

1. **Upload a contract** (PDF or DOCX).
2. **Review extracted clauses** and risk analysis.
3. **Override risk levels** if needed.
4. **Download the JSON or PDF report.**
5. **Ask questions** about the contract using the Q&A feature.

---

## Example Output

```json
{
  "clauses": {
    "Termination": "Either party may terminate with 7 days written notice...",
    "Payment": "Total project cost: $150,000 USD...",
    "NDA": "Both parties acknowledge access to highly sensitive proprietary information...",
    "Indemnity": "PARTIAL: While there is no explicit indemnification clause...",
    "Data Privacy": "PARTIAL: Section 7 (COMPLIANCE) states that ..."
  },
  "overall_risk": "medium"
}
```

---

## License

This project is for educational and demonstration purposes. For commercial use, please consult the license terms of the underlying LLMs and APIs.

---

## Acknowledgements
- [LangChain](https://github.com/langchain-ai/langchain)
- [Together AI](https://www.together.ai/)
- [Streamlit](https://streamlit.io/)
- [Hugging Face](https://huggingface.co/)