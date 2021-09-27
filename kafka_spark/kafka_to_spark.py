import findspark

findspark.init()

import os

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 pyspark-shell'

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext(appName="PythonSparkStreamingKafka")
ssc = StreamingContext(sc, 2)

dks = KafkaUtils.createDirectStream(ssc, topics=['test_Thinh'],
                                    kafkaParams={"metadata.broker.list": "localhost:9092"})

lines = dks.map(lambda x: x[1])
counts = lines.flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)
counts.pprint()

ssc.start()
ssc.awaitTermination()

# spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0 kafka_to_spark.py



# spark = SparkSession \
#     .builder \
#     .appName("APP") \
#     .getOrCreate()

# df = spark \
#     .readStream \
#     .format("kafka") \
#     .option("kafka.bootstrap.servers", "localhost:9092") \
#     .option("subscribe", "sparktest") \
#     .option("startingOffsets", "earliest") \
#     .load()