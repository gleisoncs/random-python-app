FROM python:3.9-slim

RUN mkdir -p /var/log/app

WORKDIR /app
COPY app.py /app


RUN pip install flask

CMD ["python", "app.py"]
