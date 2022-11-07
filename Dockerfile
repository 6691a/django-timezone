FROM python:3.8.3-alpine


WORKDIR /app

EXPOSE 8888

COPY . .


RUN apk update \
    && apk add bash tzdata 

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt
