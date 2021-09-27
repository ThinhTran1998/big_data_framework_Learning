# from pymongo import MongoClient

from kafka import KafkaConsumer

consumer = KafkaConsumer('test_Thinh',
                         bootstrap_servers=['127.0.0.1:9092'],
                         api_version=(0, 10, 1))

# client = MongoClient('localhost:27017')
# collection = client.numtest.numtest

for message in consumer:
    # message = message.value
    # collection.insert_one(message)
    print(message, ' + ', message)
