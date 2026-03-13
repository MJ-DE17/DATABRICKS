# import dlt

# # Create Streaming Table
# @dlt.table(
#     name = "orders_streaming_table"
# )
# def orders_streaming_table():
#     df = spark.readStream.table("workspace.default.orders")
#     return df


# # Create Materialized View
# @dlt.table(
#     name = "orders_materialized_view"
# )
# def orders_materialized_view():
#     df = spark.read.table("workspace.default.orders")
#     return df

# # Batch View
# @dlt.view(
#     name="batch_orders_view"
# )
# def batch_orders_view():
#     df = spark.read.table("workspace.default.orders")
#     return df


# # Streaming View
# @dlt.view(
#     name="stream_orders_view"
# )
# def stream_orders_view():
#     df = spark.readStream.table("workspace.default.orders")
#     return df