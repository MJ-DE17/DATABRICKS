import dlt
from pyspark.sql.functions import *

# Bronze table
@dlt.table (
    name = "bronze_orders",
    comment = "Raw datas of orders"
)
def bronze_orders():
    df = spark.read.table("workspace.default.orders")
    return df

# Silver Table
@dlt.table(
    name = "silver_orders",
    comment = "Cleaned datas of orders"
)

def silver_orders():
    df = dlt.read("bronze_orders") \
        .filter(col("status") != "CANCELLED")
    return df

# Gold table (aggregated data)
@dlt.table(
  name="gold_orders_summary",
  comment="Aggregated order statistics"
)
def gold_orders_summary():

    df = dlt.read("silver_orders") \
        .groupBy("status") \
        .count()

    return df
