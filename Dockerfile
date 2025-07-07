FROM python:3.11-slim

# Instala as dependências necessárias
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Instala Flask e pynvml
RUN pip install flask nvidia-ml-py3

# Copia o código da aplicação
COPY app.py /app/app.py
WORKDIR /app

# Expõe a porta
EXPOSE 5050

# Comando de inicialização
CMD ["python", "app.py"]
