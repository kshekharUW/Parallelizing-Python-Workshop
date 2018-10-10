import os
import sys
import time
import numpy
import multiprocessing
from multiprocessing import Process, Value, Array

size = 2000000
number_processes = 8
chuck_size = size / number_processes

a = Array('d', [1.0] * size)
b = Array('d', [1.0] * size)

dot = Value('d', 0.0)
processes = [ ]

def dotproduct(dot, a, b):
  dot.value += sum(x * y for x, y in zip(a, b))

time1 = time.time()

for i in range(number_processes):
    lb = i * chuck_size
    ub = lb + chuck_size
    p = Process(target=dotproduct, args=(dot, a[lb:ub], b[lb:ub],))
    processes.append(p)
    p.start()

for p in processes:
  p.join()

time2 = time.time() - time1
print("dot product of 2 x 2000000 unit vectors = {0}".format(dot.value))
print("Time = {0}".format(time2))
