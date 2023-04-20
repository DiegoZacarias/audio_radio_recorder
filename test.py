import requests
import subprocess
import time

# Solo graba 10 segundos para probar
url = 'https://media.streambrothers.com:8342/stream'
output_file = '/Users/diego/radio_recordings/emision.mp3'
recording_time = 10  # segundos

response = requests.get(url, stream=True)
stream = response.raw

with open(output_file, 'wb') as f:
    start_time = time.time()
    while time.time() - start_time < recording_time:
        data = stream.read(1024)
        if not data:
            break
        f.write(data)
    f.close()
