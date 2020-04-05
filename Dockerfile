FROM python:3.7

COPY . /cs5224
WORKDIR /cs5224

RUN pip install -r requirements.txt

CMD make start
