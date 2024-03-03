FROM python:3.10.4-slim-buster

LABEL maitaner="sabsdaid@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password --no-create-home django-user

COPY . .

RUN chown -R www-data:www-data /app

USER www-data

CMD ["gunicorn", "core.wsgi"]