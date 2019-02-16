
ssh node-201 kafka-server-stop.sh $KAFKA_HOME/config/server.properties
ssh node-202 kafka-server-stop.sh $KAFKA_HOME/config/server.properties
ssh node-203 kafka-server-stop.sh $KAFKA_HOME/config/server.properties

ssh node-201 zookeeper-server-stop.sh $KAFKA_HOME/config/zookeeper.properties
ssh node-202 zookeeper-server-stop.sh $KAFKA_HOME/config/zookeeper.properties
ssh node-203 zookeeper-server-stop.sh $KAFKA_HOME/config/zookeeper.properties

