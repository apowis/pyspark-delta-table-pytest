# pytest-spark-quick-demo
A demo of using the pytest-spark library to test delta tables.

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

## GitHub Actions
Some of the methods I have used for the GitHub Actions are definitely sub-optimal.
I use this repo as a bit of a playground to test actions.