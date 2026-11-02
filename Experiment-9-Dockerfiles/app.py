import os
import platform
import time
from datetime import datetime

name = os.getenv("STUDENT_NAME", "Student")
repeat = int(os.getenv("REPEAT", "5"))

print(f"Hello, {name}!")
print("Python version:", platform.python_version())
print("Operating system:", platform.system())
print("Host name:", platform.node())

for i in range(1, repeat + 1):
    print(f"[{datetime.now():%H:%M:%S}] Tick {i} of {repeat}")
    time.sleep(1)

print("Program finished.")