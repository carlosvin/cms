__author__ = 'carlos'

class Server:
    def __init__(self):
        self.__test = "test"

    def run(self):
        print(self.__test)

if __name__ == 'main':
    Server().run()