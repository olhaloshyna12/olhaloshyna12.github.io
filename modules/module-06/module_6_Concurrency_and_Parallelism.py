# Module 6 exercise was completed during an in-class seminar
#Concurrency and Parallelism – Race Conditions and Synchronisation Mechanisms
#Example 1: Non Thread-Safe Code (The Problem): multiple threads trying to update a shared counter.
#This code has a race condition. The operation counter += 1 is not atomic. It involves three steps: (1) read the value, (2) increment it, (3) write the value back. A thread can be preempted after step 1, leaving the counter in an inconsistent state.
#Solution: 
import threading
# Shared resource (global variable)
counter = 0
def increment_counter():
    """A function that is NOT thread-safe."""
    global counter
    for _ in range(100000):
        # This is the critical section
        counter += 1
# Create multiple threads
threads = []
for _ in range(5):
    t = threading.Thread(target=increment_counter)
    threads.append(t)
    t.start()
# Wait for all threads to finish
for t in threads:
    t.join()
print(f"Expected final counter value: 500000")
print(f"Actual final counter value: {counter}")
# The ‘Actual’ value will almost always be less than 500,000 due to the race condition.
# Run this code several times. You will get different, incorrect results each time.
#Synchronisation Mechanisms: 
#Semaphore: A Semaphore is a generalized lock. Instead of a single key, it controls access to a resource with a fixed number of identical keys (or permits). A thread must acquire a permit to proceed. If all permits are taken, subsequent threads block until a permit is released by another thread.
#Example: Python Example with threading.Semaphore (Limiting Concurrent Downloads):
#Solution: 
import threading
import time
import random
# Suppose we only have 3 available download slots
download_slots = threading.Semaphore(3)
def download_file(filename):
    # Acquire a download slot. If none are free, block here.
    with download_slots:
        print(f"{threading.current_thread().name} is downloading {filename}...")
        # Simulate download time
        time.sleep(random.uniform(1, 3))
        print(f"{threading.current_thread().name} finished downloading {filename}")
# Simulate 10 files to download
files = [f"file_{i}.zip" for i in range(10)]
threads = []
for filename in files:
    t = threading.Thread(target=download_file, args=(filename,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
# You will see that only 3 threads are ever downloading at the same time in this solution. 
#Monitors: A Monitor is a higher-level synchronization construct that bundles shared data with the synchronization operations (methods) that act upon it. It's not a separate primitive in Python like a Lock or Semaphore; it's a design pattern implemented using them.
#Example: Python Example Implementing the Monitor Pattern
#Python provides the threading.Condition class, which combines a Lock with additional logic for waiting and notification. A Condition is the primary tool for building monitors.
#Solution: 
import threading
class BoundedBuffer:
    """A thread-safe bounded buffer (queue) implementing the Monitor pattern."""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [] # The shared data
        self.lock = threading.Lock() # The monitor lock
        # Condition variables to coordinate producers and consumers
        self.not_full = threading.Condition(self.lock)  # "The buffer is not full"
        self.not_empty = threading.Condition(self.lock) # "The buffer is not empty"
    def put(self, item):
        """Add an item to the buffer. Block if the buffer is full."""
        with self.lock: # Acquire the monitor lock for the entire method
           
 # Wait until there is space in the buffer
            while len(self.buffer) == self.capacity:
                self.not_full.wait() # Releases lock, blocks, re-acquires lock on wakeup
           
 # Critical Section Start
            self.buffer.append(item)
           
 # Critical Section End
            # Notify a waiting consumer that the buffer is no longer empty
            self.not_empty.notify()
    def get(self):
        """Remove and return an item from the buffer. Block if the buffer is empty."""
        with self.lock: # Acquire the monitor lock for the entire method
           
 # Wait until there is an item to consume
            while len(self.buffer) == 0:
                self.not_empty.wait() # Releases lock, blocks, re-acquires lock on wakeup
            
# Critical Section Start
            item = self.buffer.pop(0)
            # Critical Section End
            # Notify a waiting producer that the buffer is no longer full
            self.not_full.notify()
            return item
# Usage: Producer-Consumer
buffer = BoundedBuffer(5)
def producer():
    for i in range(20):
        buffer.put(i)
        print(f"Produced {i}")
def consumer():
    for _ in range(20):
        item = buffer.get()
        print(f"Consumed {item}")
        time.sleep(0.1) # Simulate work
prod_thread = threading.Thread(target=producer)
cons_thread = threading.Thread(target=consumer)
prod_thread.start()
cons_thread.start()
prod_thread.join()
cons_thread.join()
#Concurrency Issues: 
#Race Conditions: A race condition occurs when the behaviour of a software system depends on the relative timing of events, such as the order in which threads are scheduled. The output is non-deterministic and becomes incorrect when the "wrong" interleaving happens.
#Example: The Lost Update
#Solution: 
import threading
balance = 100  # Shared resource
def update_balance(amount):
    global balance
    # Simulate a non-atomic operation (read-modify-write)
current_balance = balance   # Thread A reads 100 | Thread B reads 100
    # A context switch can happen here
    new_balance = current_balance + amount
    balance = new_balance       # Thread A writes 100+50=150 | Thread B writes 100+20=120
# Thread A: deposit 50
thread_a = threading.Thread(target=update_balance, args=(50,))
# Thread B: deposit 20
thread_b = threading.Thread(target=update_balance, args=(20,))
thread_a.start()
thread_b.start()
thread_a.join()
thread_b.join()
print(f"Final balance: {balance}") # Could be 120, 150, or 170? The 170 update is lost.
#N.B.: The correct final balance should be 170, but one of the updates is lost because both threads read the old value before either wrote the new one.
#Deadlock: A situation where two or more threads are permanently blocked, each waiting for a resource held by the other. They are stuck in a cyclic dependency with no way out.
#Example: The Dining Philosophers 
#Solution: 
import threading
# Forks are locks
fork_a = threading.Lock()
fork_b = threading.Lock()
fork_c = threading.Lock()
def philosopher(name, left_fork, right_fork):
    with left_fork:
        print(f"{name} picked up left fork.")
        # A context switch here can lead to deadlock!
        with right_fork:
            print(f"{name} picked up right fork and is eating.")
    print(f"{name} is done.")
# Create philosophers who pick up left then right
t1 = threading.Thread(target=philosopher, args=("Philosopher A", fork_a, fork_b))
t2 = threading.Thread(target=philosopher, args=("Philosopher B", fork_b, fork_c))
t3 = threading.Thread(target=philosopher, args=("Philosopher C", fork_c, fork_a)) # Circular wait!
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join() # The program will likely hang here forever.
#Livelock: Similar to a deadlock because threads are unable to make progress. However, they are not blocked; they are actively performing work that is effectively useless in resolving the contention. They are like two people trying to pass each other in a hallway but always stepping into the same direction.
#Example & Solution: 
import threading
import time
husband_path = "right"
wife_path = "left"
lock = threading.Lock()
def husband():
    global husband_path
    while True:
        with lock:
            if husband_path != wife_path:
                print("Husband passes successfully!")
                break
            else:
                print("Husband steps aside...")
                husband_path = "left" # He moves left to let her pass
                # A context switch often happens here
                time.sleep(0.1) # Simulate work/decision time
def wife():
    global wife_path
    while True:
        with lock:
            if wife_path != husband_path:
                print("Wife passes successfully!")
                break
            else:
                print("Wife steps aside...")
                wife_path = "right" # She moves right to let him pass
                time.sleep(0.1) # Simulate work/decision time
t1 = threading.Thread(target=husband)
t2 = threading.Thread(target=wife)
t1.start()
t2.start()
t1.join()
t2.join()
# The threads may repeatedly change their state, printing "steps aside..." forever.
#Seminar Task 2: Using simple Python code to use threading and synchronisation mechanisms (e.g., threading lock) to ensure thread safety.
#The Problem: Unsafe Counter without Synchronization
#First, let's see what happens without any synchronization. We'll create multiple threads that all try to increment a shared counter.
import threading
import time
# This is our shared global variable
counter = 0
def unsafe_increment():
"""This function is NOT thread-safe."""
    global counter
for _ in range(100000):  # Each thread increments 100,000 times
        # This operation is not atomic: read -> modify -> write
        temp = counter  # Read current value
        temp = temp + 1  # Modify value
        counter = temp  # Write new value
        # A context switch can happen between any of these steps!
# Create multiple threads
threads = []
for i in range(5):  # Let's create 5 threads
    t = threading.Thread(target=unsafe_increment)
    threads.append(t)
    t.start()
# Wait for all threads to finish
for t in threads:
    t.join()
print(f"Expected final value: 500000")
print(f"Actual final value: {counter}")
# The actual value will be less than 500,000 due to race conditions
#Why this fails: The operation counter += 1 is not atomic. Threads can interrupt each other between reading and writing, causing lost updates.
#Solution: Using threading.Lock for Synchronization
#Now let's fix this using a lock to make the critical section thread-safe.
import threading
import time
# Shared variable
counter = 0
# Create a lock object
lock = threading.Lock()
def safe_increment():
    """This function is thread-safe using a lock."""
    global counter
    for _ in range(100000):
        # Acquire the lock before entering critical section
        lock.acquire()
        try:
            # Critical section - only one thread can execute this at a time
            temp = counter
            temp = temp + 1
            counter = temp
            # Simulate some processing time to make race conditions more obvious
            time.sleep(0.000001)
        finally:
            # Always release the lock, even if an error occurs
            lock.release()
# Create and run threads
threads = []
for i in range(5):
    t = threading.Thread(target=safe_increment)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f"Expected final value: 500000")
print(f"Actual final value: {counter}")  # This will now always be correct!
