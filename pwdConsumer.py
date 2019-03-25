import string
import threading
import queue
from itertools import product, chain

class pwdConsumer(threading.Thread):

    def __init__(self, queue, condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition

    def run(self):
        while (True):
            pwd = None
            self.condition.acquire()
            try:
                pwd = self.queue.get(block=False)

                your_list = string.ascii_lowercase + ''+ string.ascii_uppercase +''+string.digits
                complete_list = []

                print("Start bruteforce")

                for current in range(4):
                    a = [i for i in your_list]
                    for y in range(current):
                        a = [x + i for i in your_list for x in a]
                    complete_list = complete_list + a

                print("End bruteforce")

                for val in complete_list:
                    if(pwd.check(val)):
                        print("The password is " + val)
                self.condition.notify()
            except queue.Empty:
                self.condition.wait()
            self.condition.release()

