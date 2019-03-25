import threading
import queue
from bruteforce2.Password import Password

class pwdProducer(threading.Thread):

    def __init__(self,queue, conditon):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = conditon

    def run(self):
        while(True):
            password = input("Password: ")
            self.condition.acquire()
            try:
                self.queue.put(Password(password), block=False)
                self.condition.notify()
            except queue.Full:
                self.condition.wait()
            self.condition.release()