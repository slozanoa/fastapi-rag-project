import os
from pathlib import Path

# Rutas base
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DB_DIR = BASE_DIR / "db"

# Configuración de archivos
PDF_PATH = DATA_DIR / "estadistica.pdf"

# Configuración del modelo
MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
MAX_TOKENS = 1000
TEMPERATURE = 0

# Asegurarse que las carpetas necesarias existen
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True) 