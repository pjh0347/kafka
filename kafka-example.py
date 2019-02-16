#!/usr/bin/env python

import threading, logging, time
import multiprocessing
from kafka import KafkaConsumer, KafkaProducer


BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'test'
GROUP_ID = 'test_group_id'


class Producer(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self, name=name)
        self.stop_event = threading.Event()
        
    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)

        i = 0
        while not self.stop_event.is_set():
            msg = "msg-{}".format(i)
            i += 1
            producer.send(TOPIC, bytes(msg))
            logging.info("[SEND] %s", msg)
            time.sleep(1)

        producer.close()

#class Consumer(multiprocessing.Process):
class Consumer(threading.Thread):

    def __init__(self, name):
        #multiprocessing.Process.__init__(self, name=name)
        #self.stop_event = multiprocessing.Event()
        threading.Thread.__init__(self, name=name)
        self.stop_event = threading.Event()
        
    def stop(self):
        self.stop_event.set()
        
    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS,
                                 auto_offset_reset='latest',
                                 #auto_offset_reset='earliest',
                                 group_id=GROUP_ID,
                                 consumer_timeout_ms=1000)
        consumer.subscribe([TOPIC])

        while not self.stop_event.is_set():
            for message in consumer:
                logging.info("[RECV] %s", message.value)
                #time.sleep(3)
                if self.stop_event.is_set():
                    break

        consumer.close()


def main():
    tasks = [
        Producer('Producer-1'),
        Producer('Producer-2'),
        Consumer('Consumer-1'),
        Consumer('Consumer-2'),
        Consumer('Consumer-3'),
        Consumer('Consumer-4'),
        Consumer('Consumer-5'),
    ]

    for t in tasks:
        t.start()

    time.sleep(60)
    
    for task in tasks:
        task.stop()

    for task in tasks:
        task.join()
        
        
if __name__ == "__main__":
    logging.basicConfig(
        format='[%(asctime)s] [%(levelname)s] [%(processName)s] [%(threadName)s] %(message)s',
        level=logging.INFO
        )
    main()
