import threading
import time


class SingThread(threading.Thread):
    def __init__(self, name, a):
        super().__init__()
        self.name = name
        self.a = a

    def run(self, ):
        print("线程的名字是%s,接受的参数是%s" % (self.name, self.a))
        for x in range(1, 6):
            print("我在唱七里香")
            time.sleep(1)


class DanceThread(threading.Thread):
    def __init__(self, name, a):
        super(DanceThread, self).__init__()
        self.name = name
        self.a = a

    def run(self):
        print("线程的名字是%s,接受的参数是%s" % (self.name, self.a))
        for x in range(1, 6):
            print("我在跳钢管舞")
            time.sleep(1)


def main():
    tsing = SingThread("sing", "猪八戒")
    tdance = DanceThread("dance", "猪悟能")
    tsing.start()
    tdance.start()



if __name__ == '__main__':
    main()
