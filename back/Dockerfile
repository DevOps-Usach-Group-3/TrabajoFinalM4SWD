FROM maven:3.6.3-jdk-11-slim

RUN apt-get update && apt-get install dos2unix
COPY . /code/
COPY ./drivers /code/drivers
WORKDIR /code
RUN mvn install -Dmaven.test.skip

