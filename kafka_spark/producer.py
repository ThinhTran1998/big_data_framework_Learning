from json import dumps
from time import sleep

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'),
                         api_version=(0, 10, 1))

print('producer created')

for e in range(1000):
    data = {'number': e}
    print(e)
    producer.send('test_Thinh', value=data)
    sleep(2)

producer.flush()


