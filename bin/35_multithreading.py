print("USING LOCKING multithreading")
print("-"*20)
# --------------
import time

start_time = time.time()

from threading import Lock
my_lock = Lock()
def my_square_function(my_list):
    my_lock.acquire()
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)
    my_lock.release()



L = [10, 20, 30, 40, 50]

from threading import Thread

my_thread_1 = Thread(target=my_square_function, args=[L])
my_thread_2 = Thread(target=my_square_function, args=[L])

my_thread_1.start()
# this will start the thread and goto next line. Which means it will not wait for
# thread execution to complete

my_thread_2.start()
# this will start the thread and goto next line. Which means it will not wait for
# thread execution to complete

# Wait here till both threads completes execution
my_thread_1.join()
my_thread_2.join()

end_time = time.time()

print("Time Taken:", end_time-start_time)
print("Time Taken (roundup):", round(end_time-start_time, 3))

print("#"*40, end="\n\n")
################################