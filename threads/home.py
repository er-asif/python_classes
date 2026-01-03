import threading
from helpers import DoSomething



if __name__ == "__main__":
    t1 = DoSomething("Mohammad Asif")
    t1.start()
    t2 = DoSomething("Manish Yadav")
    t2.start()
    t1.join()
    t2.join()