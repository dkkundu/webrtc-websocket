# Use the official Python 3.10 image as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY . /app
COPY ./requirements.txt /app/requirements.txt

#RUN apk add postgresql-dev gcc musl-dev
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

