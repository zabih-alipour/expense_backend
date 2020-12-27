FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

ENV FLASK_APP=src/app.py

RUN source vevn/bin/activate

RUN flask run