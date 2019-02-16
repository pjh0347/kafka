
ssh node-201 zookeeper-server-start.sh -daemon $KAFKA_HOME/config/zookeeper.properties
ssh node-202 zookeeper-server-start.sh -daemon $KAFKA_HOME/config/zookeeper.properties
ssh node-203 zookeeper-server-start.sh -daemon $KAFKA_HOME/config/zookeeper.properties

ssh node-201 kafka-server-start.sh -daemon $KAFKA_HOME/config/server.properties
ssh node-202 kafka-server-start.sh -daemon $KAFKA_HOME/config/server.properties
ssh node-203 kafka-server-start.sh -daemon $KAFKA_HOME/config/server.properties

