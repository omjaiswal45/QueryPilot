"""FastAPI application entrypoint.

TODO:
- Register real routers from routes/ (replace the throwaway /health check below).
- Register the exception handler from exceptions/handler.py.
"""
from fastapi import FastAPI

from configurations.env_intializer import env
from configurations.config_registry import ConfigRegisterer

ConfigRegisterer.register_configs(env)

app = FastAPI(title="QueryPilot")


@app.get("/health")
def health_check():
    return {"status": "ok"}
