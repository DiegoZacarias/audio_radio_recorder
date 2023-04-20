import requests
import subprocess
import time
from datetime import datetime, time as t

url = 'https://media.streambrothers.com:8342/stream'
output_file = '/Users/diego/radio_recordings/emision_test1.mp3'

# Set start and end time
start_time = datetime.now().replace(hour=11, minute=30, second=0, microsecond=0)
# end_time = datetime.now().replace(hour=14, minute=10, second=0, microsecond=0)
end_time = datetime.now().replace(hour=13, minute=20, second=0, microsecond=0)

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

# No se abre automáticamente el archivo grabado
