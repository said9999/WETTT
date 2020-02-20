FROM python:3.7

RUN pip install flask && pip install gunicorn
COPY . /cs5224
WORKDIR /cs5224

CMD make start
