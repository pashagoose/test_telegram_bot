# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install pyTelegramBotAPI

COPY echo_bot.py echo_bot.py

CMD [ "python3", "echo_bot.py" ]

