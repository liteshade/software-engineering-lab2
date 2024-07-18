import os
from dotenv import load_dotenv
from chromadb.config import Settings

load_dotenv("config.env")

# Define the folder for storing database
PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY')

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
        chroma_db_impl='duckdb+parquet',
        anonymized_telemetry=False
)
