from kafka import KafkaConsumer
from json import loads
import time

time.sleep(50)

import hdfs

try:

    consumer = KafkaConsumer(
        'hb',
        bootstrap_servers=['kafka:29092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))

except:
  raise Exception('kafka connect error')


for message in consumer:
    message = message.value
    hdfs.write_to_hdfs(str(message))
    print(message)
    
    