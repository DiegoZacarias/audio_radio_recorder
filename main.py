import requests
import subprocess
import time
from datetime import datetime, time as t

url = 'https://media.streambrothers.com:8342/stream'

# Set start and end time
start_time = datetime.now().replace(hour=11, minute=26, second=0, microsecond=0)
end_time = datetime.now().replace(hour=14, minute=10, second=0, microsecond=0)

# Nombre del archivo: emisora + fecha + hora
date_str = datetime.now().strftime('%Y_%m_%d')
output_file = f'/Users/diego/radio_recordings/{date_str}_emision_cardinal_deportivo.mp3'

# Open stream
response = requests.get(url, stream=True)
stream = response.raw

print('recording stream')

# Record stream
with open(output_file, 'wb') as f:
    while datetime.now() < end_time:
        if datetime.now() >= start_time:
            data = stream.read(1024)
            if not data:
                break
            f.write(data)
    f.close()

# Close stream
stream.close()

print('stream recording finished')
