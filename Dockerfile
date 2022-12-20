FROM jupyter/pyspark-notebook
WORKDIR /home/
ADD pyproject.toml ./
RUN pip install .
ADD ./tests ./tests/
RUN pytest
