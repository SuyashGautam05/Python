import time
# timestamp = time.strftime('%H:%M:%S')  ##24hours Format
timestamp = time.strftime('%I:%M:%S')     # 12 hours format

print(timestamp)
timestamp = time.strftime('%I')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime