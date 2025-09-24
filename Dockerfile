FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PORT=8080
WORKDIR /app

COPY link-extractor/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY link-extractor/server.py .
COPY link-extractor/static ./static

EXPOSE 8080
CMD ["gunicorn","-b","0.0.0.0:${PORT}","-w","2","--threads","8","server:app"]
