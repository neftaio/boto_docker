FROM python:3.8

RUN apt-get update
RUN pip install boto
COPY ./.boto /root/.boto
COPY ./change_permisions_files.py /root/

WORKDIR /root/