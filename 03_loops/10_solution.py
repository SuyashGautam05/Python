import time

# print(time.ctime())

wait_time = 1
max_retries = 6
attempts = 0

while attempts < max_retries:
    print("Attempts", attempts + 1, "- wait time", wait_time)
    time.sleep(wait_time)
    wait_time = wait_time * 2
    attempts = attempts + 1
