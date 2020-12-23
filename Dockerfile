FROM ubuntu:latest
RUN apt-get update -y &&\
    apt-get install -y python3-pip python3-dev
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python3" ]
CMD [ "app/app.py" ]