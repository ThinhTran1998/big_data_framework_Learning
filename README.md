-	Run zookeeper server
zkserver

-	Run kafka server
.\bin\windows\kafka-server-start.bat .\config\server.properties

-	Creating Topics:
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

-	Test:
kafka-console-producer.bat --broker-list localhost:9092 --topic test_Thinh

kafka-console-consumer.bat –bootstrap-server localhost:9092 –topic test_Thinh
