FROM python:3.10.4-slim-buster
LABEL maitaner="sabsdaid@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

USER django-user

ENTRYPOINT ["gunicorn", "core.wsgi"]
