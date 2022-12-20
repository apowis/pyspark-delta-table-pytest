# pytest-spark-quick-demo
A tiny demo of using the pytest-spark library with an easy to use Dockerfile

## Instructions To Test

Create a Python environment with version greater than *3.7.2*, and pip install.

You can then run the pytest and see the results.

For instance, using conda;
```
conda create --name py310 python=3.10
conda activate py310
pip install .
pytest
```

You can also just use the provided Dockerfile using the command `docker build .`.
