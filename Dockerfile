FROM python:3

RUN apt-get update

RUN pip install tweepy

RUN mkdir /root/src
WORKDIR /root/src