import time
import threading
import random
start_vent_thread_event = threading.Event()
open_vent_event = threading.Event()
close_vent_event = threading.Event()

##threads work by starting them. They dont really stop. You can create
##an event to start and stop by using set/clear/wait. set turns wait to true
##clear turns wait to false. This is handy in a while loop.

def temperature_readout():
    my_thread = threading.Thread(target=open_close_vent_thread,daemon=True)
    my_thread.start()
    while True:
        command = int(input("1 for open, 2 for close: "))
        if command is 1:
            start_vent_thread_event.set()
            open_vent_event.set()
        elif command is 2:
            start_vent_thread_event.set()
            close_vent_event.set()
        time.sleep(4)


def open_close_vent_thread():
    while start_vent_thread_event.wait():
        print("open close thread started")
        if open_vent_event.wait():
            time.sleep(2)
            print("I am opening the vent")
            open_vent_event.clear()

        if close_vent_event.wait():
            time.sleep(2)
            print("I am closing the vent")
            close_vent_event.clear()
        start_vent_thread_event.clear()

if __name__ == '__main__':
    temperature_readout()
