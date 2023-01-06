"""
Simple example of how to use the pip package pytest-spark
to test delta tables.

Note that the imported object spark_session is a pytest fixture,
but I have type hinted it as a SparkSession. This is because it
reacts almost exactly the same as if it was a SparkSession, and
it makes the autocompletion and syntax highlighting play nicely.
"""
from pyspark.sql.dataframe import DataFrame as SqlDataFrame
from pyspark.sql.types import Row
from pyspark.sql import SparkSession
import pytest
from pytest_spark import spark_session


TABLE_NAME = "temp_table"
DROP_STATEMENT = f"drop table if exists {TABLE_NAME}"


# Scope set to "module", so that this fixture only
# gets run once within this file.
@pytest.fixture(scope="module", autouse=True)
def create_delta_table(spark_session: SparkSession):
    """
    Creates a new delta table, making sure to drop the table
    first, incase it still exists.
    Once this module is complete, it drops the table.
    """
    spark_session.sql(DROP_STATEMENT)
    df: SqlDataFrame = spark_session.createDataFrame(
        [
            {"a": 1},
        ]
    )
    df.write.saveAsTable(TABLE_NAME, format="delta")
    yield
    spark_session.sql(DROP_STATEMENT)


def test_simple_dataframe(spark_session: SparkSession):
    df = spark_session.read.table(TABLE_NAME)
    assert df.first() == Row(a=1)
