FROM python:3.11-slim

# Créer un utilisateur non-root compatible Debian slim
RUN groupadd appgroup && useradd -r -g appgroup appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

CMD ["python", "app.py"]