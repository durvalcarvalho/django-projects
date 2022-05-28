FROM node

EXPOSE 8000

RUN mkdir /src

WORKDIR /src

COPY frontend /src

# Install parcel-bundler
RUN npm -g install parcel-bundler
