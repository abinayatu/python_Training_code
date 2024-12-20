"""
multithreading
"""
print("WITHOUT using multithreading")
print("-"*20)
# --------------
import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40, 50]
my_square_function(L)
my_cube_function(L)

end_time = time.time()

print("Time Taken:", end_time-start_time)
print("Time Taken (roundup):", round(end_time-start_time, 3))

print("#"*40, end="\n\n")
################################

print("USING multithreading")
print("-"*20)
# --------------
import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40, 50]

from threading import Thread

my_thread_1 = Thread(target=my_square_function, args=[L])
my_thread_2 = Thread(target=my_cube_function, args=[L])

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

print("WITH DELAY: WITHOUT using multithreading")
print("-"*20)
# --------------
import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40, 50]
my_square_function(L)
my_cube_function(L)

end_time = time.time()

print("Time Taken:", end_time-start_time)
print("Time Taken (roundup):", round(end_time-start_time, 3))

print("#"*40, end="\n\n")
################################

print("WITH DELAY: USING multithreading")
print("-"*20)
# --------------
import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40, 50]

from threading import Thread

my_thread_1 = Thread(target=my_square_function, args=[L])
my_thread_2 = Thread(target=my_cube_function, args=[L])

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