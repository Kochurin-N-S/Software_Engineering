from datetime import datetime
from time import sleep

for i in range(5):
    current_data_and_time = datetime.now()
    print(current_data_and_time.time())
    sleep(1)