"""Single wrapper around the Anthropic SDK — the only file that imports `anthropic` directly.

TODO:
def complete(prompt: str, system: str | None = None) -> str:
    ...

Every agent calls THIS, never the SDK directly — keeps provider-swapping and
mocking-in-tests confined to one file.
"""
