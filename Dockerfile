FROM python:3.13-alpine

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app .

CMD fastapi run main.py --port 8000
