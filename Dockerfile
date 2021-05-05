# Use the official Python image from the Docker Hub
FROM ubuntu
FROM python:latest

# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Update aptitude with new repo
RUN apt-get update

# Install software
RUN apt-get install -y git

# Make a new directory to put our code in.
RUN mkdir /code

# Change the working directory.
# Every command after this will be run from the /code directory.
WORKDIR /code

## Copy the requirements.txt file.
#COPY . /code/
RUN git clone https://github.com/abhisheksahu92/Phone-Directory.git

# Upgrade pip
RUN pip install --upgrade pip

# Install the requirements.
RUN pip install -r /code/Phone-Directory/requirements.txt