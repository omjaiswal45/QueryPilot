"""Single FastAPI exception handler, registered once in main.py.

TODO:
- Register an exception_handler for ApiError that dispatches on the concrete subclass
  and returns the standard envelope: {success: false, message, errors?}.
- Only include stack traces when settings.ENV == "dev".
"""
