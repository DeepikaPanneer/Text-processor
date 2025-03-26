import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def lambda_handler(event, context):
    # Initialize SparkSession
    spark = SparkSession.builder.appName("LambdaPySpark").getOrCreate()

    # Sample data
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    columns = ["Name", "Age"]

    # Create DataFrame
    df = spark.createDataFrame(data, columns)

    # Simple transformation: Increase age by 1
    df_transformed = df.withColumn("Age", col("Age") + 1)

    # Convert to JSON
    result = df_transformed.toJSON().collect()

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }