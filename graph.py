from langgraph.graph import StateGraph, END, START
from clause_extractor import extract_clauses
from risk_classifier import classify_risks
from report_generator import generate_report
from state_schema import State

def ingest_document(state):
    # Return a new State with text and metadata
    return State(
        text=state.text,
        metadata=getattr(state, 'metadata', {})
    )

def handle_missing_or_high_risk(state):
    # Just pass through for now
    return state

def get_graph_executor():
    graph = StateGraph(State)
    graph.add_node("Ingest", ingest_document)
    graph.add_node("ExtractClauses", extract_clauses)
    graph.add_node("ClassifyRisks", classify_risks)
    graph.add_node("HandleIssues", handle_missing_or_high_risk)
    graph.add_node("GenerateReport", generate_report)
    graph.add_edge(START, "Ingest")
    graph.add_edge("Ingest", "ExtractClauses")
    graph.add_edge("ExtractClauses", "ClassifyRisks")
    graph.add_edge("ClassifyRisks", "HandleIssues")
    graph.add_edge("HandleIssues", "GenerateReport")
    graph.add_edge("GenerateReport", END)
    return graph.compile() 