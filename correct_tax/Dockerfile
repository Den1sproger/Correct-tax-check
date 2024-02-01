FROM python:3.10


ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


RUN pip install --upgrade pip

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt


WORKDIR /app


COPY . .