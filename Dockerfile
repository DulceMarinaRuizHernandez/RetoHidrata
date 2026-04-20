FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

ENV PYTHONPATH=/app
ENV FLET_WEB_PORT=$PORT

CMD ["python", "app.py"]