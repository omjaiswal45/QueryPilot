"""App DB access for schema-sync bookkeeping (which tables have been indexed, last sync
time) — distinct from the embedding vectors themselves, which live in
infrastructures/vectorstore/pgvector_store.py.

TODO: mark_table_indexed(table_name), get_last_sync_time()
"""
