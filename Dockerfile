FROM debian:buster-slim

MAINTAINER Till von Ahnen "xoryouyou@gmail.com"

ENV DEBIAN_FRONTEND noninteractive 
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN apt-get update && apt-get install git python-pip -y &&\
rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/xoryouyou/pi-hole-influx.git
WORKDIR pi-hole-influx

RUN pip install -r requirements.txt

RUN apt-get remove --purge -y git python-pip

CMD ["python", "piholeinflux.py"]
