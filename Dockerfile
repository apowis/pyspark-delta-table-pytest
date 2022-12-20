FROM apache/spark-py
WORKDIR /home/
ADD pyproject.toml ./
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install .
ADD ./tests ./tests/
RUN python3 -m pytest
