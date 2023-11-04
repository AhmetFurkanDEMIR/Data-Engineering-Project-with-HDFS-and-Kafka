![](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) ![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white) ![](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)
# Data Engineering Project with HDFS and Kafka

![](/images/map.png)

A project to create a data pipeline with data taken from Hepsiburada data engineering case study.

* [docker-compose.yml](/docker-compose.yml)


* [config-hadoop](/config-hadoop)


* [Producer](/docker/producer/)
    
    * [Dockerfile](/docker/producer/Dockerfile) 

    * [HB data](/docker/producer/hb-data.json)

    * [Kafka producer](/docker/producer/kafka_producer.py)

    * [requirements](/docker/producer/requirements.txt)


* [Consumer](/docker/consumer/)

    * [Dockerfile](/docker/consumer/Dockerfile) 

    * [Kafka consumer](/docker/consumer/kafka_consumer.py)

    * [requirements](/docker/consumer/requirements.txt)

    * [HDFS](/docker/consumer/hdfs.py)

### Steps

Open an Ubuntu machine via AWS EC2 for the project.

![](/images/instance.png)

Open the necessary ports on the machine through the firewall.

![](/images/ingress.png)

You also need to open the necessary ports with the operating system.

```bash
sudo ufw allow 9870
sudo ufw allow 8080
sudo ufw allow 8088
```

Then, stand up the docker images.

```bash
docker-compose up --build
```

One minute after the images stand up, data begins to be written to the Kafka topic and activity begins in the data pipeline.


Data from Kafka topic. IP:8080 or [0.0.0.0:8080](http://0.0.0.0:8080)
![](/images/kafka_ui.png)


Hadoop HDFS interface. IP:9870 or [0.0.0.0:9870](http://0.0.0.0:9870)
![](/images/hdfs_datanode.png)


Data from HDFS. IP:9870 or [0.0.0.0:9870](http://0.0.0.0:9870)
![](/images/hdfs_data.png)


Hadoop cluster interface. IP:8088 or [0.0.0.0:8088](http://0.0.0.0:8088)
![](/images/hadoop.png)

[Ahmet Furkan Demir](https://ahmetfurkandemir.com/)
