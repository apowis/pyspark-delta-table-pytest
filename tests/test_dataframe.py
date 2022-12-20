"""
Simple example of how to use the pip package pytest-spark
Note that the imported object spark_session is a pytest fixture,
but I have type hinted it as a SparkSession.
This is because it reacts almost exactly the same as if it was a
SparkSession, and it makes the autocompletion and syntax highlighting
play nicely.
"""
from pyspark.sql.types import Row
from pytest_spark import spark_session
from pyspark.sql import SparkSession


def test_simple_dataframe(spark_session: SparkSession):
    df = spark_session.createDataFrame([
        {"a": 1}
    ])
    assert df.first() == Row(a=1)
