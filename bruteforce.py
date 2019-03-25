import threading
import queue
from bruteforce2.pwdConsumer import pwdConsumer
from bruteforce2.pwdProducer import pwdProducer

queue = queue.Queue(maxsize=10)
condition = threading.Condition()

producer = pwdProducer(queue, condition)
consumer = pwdConsumer(queue, condition)

producer.start()
consumer.start()

producer.join()
consumer.join()