#import threading
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done sleeping...{seconds}"

#Manual way of working with threads:
#1)
# #Define two threads
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# #start the threads
# t1.start()
# t2.start()

# #wait for threads to finish running
# t1.join()
# t2.join()

#2)
# threads = [] #List of threads

# #start 10 threads using a loop
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# #wait for threads to finish using a loop.
# for thread in threads:
#     thread.join()

#Using ThreadPoolExecutor
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)

#     print(f1.result())
#     print(f2.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs) #map runs the method "do_something" for each value in "secs".

    #"results" returned in the order that they were started.
    #threads are automatically "joined"
    for result in results:
        print(result)
    
    # results = [executor.submit(do_something, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())



finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s).')