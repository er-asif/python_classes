# thread function
import time
import threading

def dosomething(person_name):
    print(f"Thead name is {threading.current_thread().name} and ID is {threading.get_ident()}")
    print(f"Doing Something for {person_name}....")
    time.sleep(1)
    print(f"Done Something. for {person_name}")
