FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN pip install flask

CMD ["python", "webhook_listener.py"]