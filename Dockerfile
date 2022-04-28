#pull official base image
FROM python:3.8.10-alpine 

#set work directory
WORKDIR /code

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONBUFFERED 1 

#install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt  . 
RUN pip install -r requirements.txt 

#to get rid of all warnings you may also want to add the following entries to the builder
#part of your Dockerfile
ARG DEBIAN_FRONTEND=noninteractive 
ARG DEBCONF_NOWARNINGS="yes"



#copy project 
COPY . .
RUN adduser -D user 
RUN chown user:user -R /code/ 
RUN chmod +x /code 
USER user 
