FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /mycode
WORKDIR /mycode
COPY . /mycode/
RUN pip install -r requirements.txt
