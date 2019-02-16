
kafka-topics.sh --create --zookeeper node-201:2181 --replication-factor 3 --partitions 20 --topic test
kafka-topics.sh --list --zookeeper node-201:2181
kafka-topics.sh --describe --zookeeper node-201:2181 --topic test
#kafka-topics.sh --delete --zookeeper node-201:2181 --topic test

kafka-console-producer.sh --broker-list node-201:9092,node-202:9092,node-203:9092 --topic test
kafka-console-consumer.sh --zookeeper node-201:2181 --topic test --from-beginning

