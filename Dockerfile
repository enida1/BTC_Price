# syntax=docker/dockerfile:1

#Define the base image
FROM python:3.8

# Set the working directory
WORKDIR /MSD


# Install pip requirements
COPY requirements.txt requirements.txt

EXPOSE 8080:8080

RUN pip3 install -r requirements.txt

# 
COPY . .



CMD [ "python3", "-u", "python_price.py"]
