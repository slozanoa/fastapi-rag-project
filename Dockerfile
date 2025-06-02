# Imagen base oficial de Python slim
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias de sistema (para compilaciones si hace falta)
RUN apt-get update && apt-get install -y build-essential curl && rm -rf /var/lib/apt/lists/*

# Copiar archivo de requerimientos
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar toda la app
COPY . .

# Exponer el puerto 8000 para la app
EXPOSE 8000

# Comando para ejecutar la app con Uvicorn en modo debug para mejor logging
CMD ["uvicorn", "src.core.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level"