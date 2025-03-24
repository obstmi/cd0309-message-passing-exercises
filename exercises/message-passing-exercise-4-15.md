## Start Kafka environment
docker pull apache/kafka-native:4.0.0
docker run -p 9092:9092 apache/kafka:4.0.0
## Create Kafka topic 'orders'
bin/kafka-topics.sh --create --topic orders --bootstrap-server localhost:9092
## Run Kafka consumer on topic 'orders'
bin/kafka-console-consumer.sh --topic orders --from-beginning --bootstrap-server localhost:9092
## Run Kafka producer on topic 'orders'
bin/kafka-console-producer.sh --topic orders --bootstrap-server localhost:9092