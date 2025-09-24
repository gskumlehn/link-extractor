FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY main.py .
COPY static ./static

EXPOSE 8080
CMD ["sh","-c","gunicorn -b 0.0.0.0:${PORT:-8080} -w ${GUNICORN_WORKERS:-2} --threads ${GUNICORN_THREADS:-8} server:app"]
