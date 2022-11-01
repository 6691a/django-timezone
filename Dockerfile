FROM python:3.8.3-alpine


WORKDIR /app

EXPOSE 8000

COPY . .



# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev \
        musl-dev py3-pillow zlib-dev jpeg-dev nodejs-current nodejs-npm curl bash libffi-dev

RUN apk --update add --no-cache g++



RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]