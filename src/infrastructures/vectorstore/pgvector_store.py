"""Embed + search table/column descriptions for the Schema-Retrieval Agent, backed by pgvector.

TODO:
def index_table_description(table_name: str, description: str) -> None:
    # embeds and upserts one row — used by a one-time schema-sync job, not per request
    ...

def search_relevant_tables(question: str, top_k: int = 5) -> list[str]:
    # embeds the question, returns the top_k closest table descriptions
    ...
"""
