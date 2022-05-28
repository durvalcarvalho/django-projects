FROM python:3.10-buster

ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

EXPOSE 8000

RUN mkdir /src

WORKDIR /src

COPY backend /src

RUN pip3 install --upgrade pip==21.* && \
    pip3 install -r requirements.txt
