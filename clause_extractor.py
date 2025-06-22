import os
from together import Together
from langchain.prompts import PromptTemplate
from prompts import CLAUSE_EXTRACTION_PROMPT
from state_schema import State
from dotenv import load_dotenv

load_dotenv()

together_client = Together(api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"])

# Only extract main clause blocks, not subheadings or bullets
CLAUSE_HEADINGS = [
    "Termination", "Payment", "NDA", "Indemnity", "Data Privacy"
]

def parse_clauses(llm_response):
    print("[DEBUG] Raw LLM response:\n", llm_response)
    clauses = {heading: "" for heading in CLAUSE_HEADINGS}
    current = None
    for line in llm_response.splitlines():
        line = line.strip()
        if not line:
            continue
        matched_heading = None
        for heading in CLAUSE_HEADINGS:
            if line.lower().startswith(heading.lower() + ":"):
                matched_heading = heading
                # Extract content after the colon, if any
                after_colon = line[len(heading) + 1:].strip()
                clauses[heading] = after_colon  # Start new block with this content
                current = heading
                break
        else:
            if current:
                # Append to the current clause, with a newline if needed
                if clauses[current]:
                    clauses[current] += "\n"
                clauses[current] += line
    # Strip trailing whitespace and newlines
    for heading in clauses:
        clauses[heading] = clauses[heading].strip()
    print("[DEBUG] Parsed clauses:", clauses)
    return clauses

def extract_clauses(state: State) -> State:
    prompt = PromptTemplate.from_template(CLAUSE_EXTRACTION_PROMPT)
    contract_text = state.text
    full_prompt = prompt.format(text=contract_text)
    response = together_client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[{"role": "user", "content": full_prompt}],
    )
    content = response.choices[0].message.content
    print("[DEBUG] LLM content returned:\n", content)
    return State(
        text=state.text,
        metadata=state.metadata,
        clauses=parse_clauses(content)
    ) 