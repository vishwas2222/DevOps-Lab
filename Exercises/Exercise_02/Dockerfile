
FROM python:3.8-slim

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir Flask

EXPOSE 15000

CMD ["python", "app.py"]

