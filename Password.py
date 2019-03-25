
class Password:

    def __init__(self, pwd):
        self.pwd = pwd

    def check(self, test):
        return self.pwd == test
