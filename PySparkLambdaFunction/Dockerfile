# Use AWS Lambda Python 3.8 base image
FROM public.ecr.aws/lambda/python:3.8

# Set PySpark version (you can adjust if needed)
ARG PYSPARK_VERSION=3.3.0

# Install Java (required by PySpark)
RUN yum install -y java-1.8.0-openjdk && \
    yum clean all

# Set JAVA_HOME for PySpark to find Java
ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
ENV PATH=$JAVA_HOME/bin:$PATH

# Install PySpark
RUN pip install --upgrade pip && \
    pip install pyspark==$PYSPARK_VERSION

# Set Spark-related environment variables
ENV SPARK_HOME="/var/lang/lib/python3.8/site-packages/pyspark"
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9-src.zip:$PYTHONPATH

# Copy your Lambda function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Set the Lambda function entry point
CMD ["app.lambda_handler"]