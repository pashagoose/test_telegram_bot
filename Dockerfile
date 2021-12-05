# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install pyTelegramBotAPI

COPY bot.py bot.py
COPY memes memes

CMD [ "python3", "bot.py" ]

