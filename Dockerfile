# Use Amazon Linux as base image (Lambda runtime compatible)
FROM amazon/aws-lambda-python:3.8

# Install Java and Hadoop dependencies for Spark
RUN yum install -y java-1.8.0-openjdk.x86_64 \
    && yum install -y wget tar gzip \
    && yum clean all

# Install PySpark
RUN pip install --upgrade pip && pip install pyspark

# Copy the Lambda function
COPY app.py ./

# Define the Lambda function entry point
CMD ["app.lambda_handler"]
