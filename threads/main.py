import threading
from helpers import dosomething
import time

start = time.perf_counter()


if __name__ == "__main__":

    print(f"Thead name is {threading.current_thread().name} and ID is {threading.get_ident()}")

    # t1 = threading.Thread(target=dosomething, args=['Mohammad Asif'])
    # t2 = threading.Thread(target=dosomething, args=['Manish Yadav'])
    # t3 = threading.Thread(target=dosomething, args=['Sambhav Verma'])

    # t1.start()
    # t2.start()
    # t3.start()
    # t1.join()
    # t2.join()
    # t3.join()

    names = ["Mohammad Asif", "Manish Yadav", "Pushkarf Singh", "Sambhav Verma"]

    threads = []
    for name in names:
        thread = threading.Thread(target=dosomething, args = [name])
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    

    finish = time.perf_counter()

    print(f"Taken {round(finish-start,2)}")