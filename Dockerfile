FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/