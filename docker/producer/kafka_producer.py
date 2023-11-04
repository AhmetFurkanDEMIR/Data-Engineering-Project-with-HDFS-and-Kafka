from json import dumps, loads
from kafka import KafkaProducer
import time

time.sleep(40)

try:

  producer = KafkaProducer(bootstrap_servers=['kafka:29092'],
                          value_serializer=lambda x: 
                          dumps(x).encode('utf-8'))
  
except:
  raise Exception('kafka connect error')

jsonFile = open("docker/producer/hb-data.json", "r+")

for line in jsonFile:
  
  jsonLine = loads(line)
  producer.send('hb', value=jsonLine)
  print(jsonLine)