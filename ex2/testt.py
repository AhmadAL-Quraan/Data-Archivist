import sys
import time

for i in range(5):
    print(f"\rProgress: {i}", end="")
    sys.stdout.flush()
    time.sleep(5)
