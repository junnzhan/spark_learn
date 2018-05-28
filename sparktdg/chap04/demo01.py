#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.master('local[*]').appName('demo01').getOrCreate()

# retail_schema = StructType([StructField('InvoiceNo', StringType, True),
#                             StructField('StockCode', StringType, True),
#                             StructField('Description', StringType, True),
#                             StructField('Quantity', IntegerType, True),
#                             StructField('InvoiceDate', TimestampType, True),
#                             StructField('UnitPrice', DoubleType, True),
#                             StructField('CustomerID', DoubleType, True),
#                             StructField('Country', StringType, True)])

df = spark.read.option('header', 'true').option('inferSchema', 'true').csv(
    '../data/retail-data/by-day/2010-12-01.csv')
df.show()
df.printSchema()
