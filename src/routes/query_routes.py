"""FastAPI router — POST /query.

TODO:
- Pydantic request model {question: str} — FastAPI validates it automatically,
  no separate validator library needed (this is your express-validator equivalent here).
- Depends() on services/query_service.py via configrations/container.py
"""
