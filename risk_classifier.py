import os
from together import Together
from langchain.prompts import PromptTemplate
from prompts import RISK_CLASSIFICATION_PROMPT
from state_schema import State
from dotenv import load_dotenv

load_dotenv()

together_client = Together(api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"])

def classify_risks(state: State) -> State:
    clauses = state.clauses
    risk_results = {}
    for clause, text in clauses.items():
        prompt = PromptTemplate.from_template(RISK_CLASSIFICATION_PROMPT)
        full_prompt = prompt.format(clause=clause, text=text)
        response = together_client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=[{"role": "user", "content": full_prompt}],
        )
        content = response.choices[0].message.content
        # Expecting: "Risk: high\nComments: ..."
        risk, comments = "unknown", ""
        for line in content.splitlines():
            if line.lower().startswith("risk:"):
                risk = line.split(":", 1)[1].strip()
            elif line.lower().startswith("comments:"):
                comments = line.split(":", 1)[1].strip()
        risk_results[clause] = {
            "text": text,
            "risk": risk,
            "comments": comments
        }
    # Calculate overall risk
    overall = "low"
    if any(v["risk"] == "high" for v in risk_results.values()):
        overall = "high"
    elif any(v["risk"] == "medium" for v in risk_results.values()):
        overall = "medium"
    return State(
        text=state.text,
        metadata=state.metadata,
        clauses=risk_results,
        overall_risk=overall
    ) 