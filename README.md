# Estadística PDF QA

API para hacer preguntas sobre documentos PDF de estadística utilizando LangChain y GPT-3.5.

## Estructura del Proyecto

```
.
├── src/
│   ├── core/           # Núcleo de la aplicación FastAPI
│   │   ├── main.py    # Punto de entrada de la API
│   │   └── models.py  # Modelos Pydantic
│   ├── services/      # Servicios de la aplicación
│   │   ├── ask.py     # Servicio de QA
│   │   ├── ingestor.py # Procesamiento de PDF
│   │   └── vector_store.py # Gestión de vectores
│   └── utils/         # Utilidades
│       └── config.py  # Configuración centralizada
├── data/             # Directorio para PDFs
├── db/              # Base de datos de vectores
└── .env             # Variables de entorno
```

## Configuración

1. Crea un archivo `.env` en la raíz del proyecto:
```
OPENAI_API_KEY=tu-api-key-aquí
```

2. Coloca tu PDF en la carpeta `data/`

## Instalación Local

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Uso Local

Para iniciar la API localmente:
```bash
uvicorn src.core.main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Despliegue con Dokploy

### Requisitos Previos
- Tener Dokploy configurado en tu VPS
- Tener acceso al repositorio Git

### Pasos para el Despliegue

1. Asegúrate de tener el archivo `.env` en tu VPS con las variables necesarias:
```bash
OPENAI_API_KEY=tu-api-key-aquí
```

2. En Dokploy:
   - Conecta tu repositorio de GitHub
   - Selecciona la rama a desplegar
   - Configura el trigger de despliegue (manual o automático)
   - Asegúrate de que los volúmenes `data` y `db` estén configurados

3. Para un despliegue manual:
   - Usa el botón "Deploy" en la interfaz de Dokploy
   - O usa el CLI de Dokploy:
     ```bash
     dokploy deploy rag
     ```

### Endpoints

- POST `/ask`
  - Recibe una pregunta sobre el contenido del PDF
  - Devuelve la respuesta y las fuentes relevantes

## Tecnologías

- FastAPI
- LangChain
- OpenAI GPT-3.5
- HuggingFace Embeddings
- ChromaDB
- Docker
- Dokploy 