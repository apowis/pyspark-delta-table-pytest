# FROM python:3.10
# USER root
# RUN apt-get update && \
#     DEBIAN_FRONTEND="noninteractive" \
#     apt-get -y install default-jre-headless

ARG IMAGE_VARIANT=slim-buster
ARG OPENJDK_VERSION=8
ARG PYTHON_VERSION=3.10

FROM python:${PYTHON_VERSION}-${IMAGE_VARIANT} AS py3
FROM openjdk:${OPENJDK_VERSION}

COPY --from=py3 / /
WORKDIR /home/
ADD pyproject.toml ./
RUN python -m pip install --upgrade pip && \
    python -m pip install .

ADD ./pytest.ini ./
ADD ./tests ./tests/
RUN python3 -m pytest
