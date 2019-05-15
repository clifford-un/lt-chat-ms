
FROM python:3.7
ENV http_proxy http://168.176.239.41:8080
ENV https_proxy http://168.176.239.41:8080
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8000
