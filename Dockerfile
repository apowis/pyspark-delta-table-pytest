FROM python:3.10
WORKDIR /home/
ADD pyproject.toml ./
RUN pip install .
ADD ./tests ./tests/
RUN pytest
