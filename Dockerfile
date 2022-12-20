FROM apache/spark-py
WORKDIR /home/
ADD pyproject.toml ./
RUN pip install .
ADD ./tests ./tests/
RUN pytest
