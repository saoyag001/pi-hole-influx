FROM python:3.7.0-alpine
MAINTAINER Till von Ahnen "xoryouyou@gmail.com"

WORKDIR /usr/src/app

COPY piholeinflux.py .
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "piholeinflux.py"]
