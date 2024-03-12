FROM python:3.10.1-slim-buster

RUN apt-get update \
&& apt-get install -y --no-install-recommends git \
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt  

ENV PORT 8080
EXPOSE $PORT

CMD exec gunicorn --bind :$PORT main:app