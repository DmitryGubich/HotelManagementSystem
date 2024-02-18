FROM python:3.11

WORKDIR /code

COPY ./requirements/dev.txt /code/requirements/dev.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements/dev.txt

COPY . /code
