FROM python:3

RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y pulseaudio

RUN pip install tweepy

RUN mkdir /root/src
WORKDIR /root/src
