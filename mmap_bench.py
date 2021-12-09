import mmap
import random
import time

file = open("C:/Users/lost/Downloads/Temp/temp-12G", "r+b", buffering=0)

map = mmap.mmap(file.fileno(), length=0)

MEGABYTES = 12 * 1024

assert map.size() == MEGABYTES * 1024 * 1024


def run_test_once():
    random_1MB = bytearray(random.getrandbits(8) for _ in range(1024 * 1024))

    start = time.time()

    for mb_index in range(MEGABYTES):
        map[mb_index * 1024 * 1024:(mb_index + 1) * 1024 * 1024] = random_1MB

    map.flush()

    end = time.time()

    return end - start


buf = bytearray(1024 * 1024)


def run_read_test_once():
    start = time.time()

    for mb_index in range(MEGABYTES):
        buf = map[mb_index * 1024 * 1024:(mb_index + 1) * 1024 * 1024]

    end = time.time()

    return end - start


for i in range(4):
    took = run_test_once()
    print(f"run {i} time: {took}s write speed: {MEGABYTES / took}MB/s")

for i in range(4):
    took = run_read_test_once()
    print(f"run {i} time: {took}s read speed: {MEGABYTES / took}MB/s")
