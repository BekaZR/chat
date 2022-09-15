FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD ./requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .