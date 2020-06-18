from concurrent.futures import ThreadPoolExecutor, as_completed
import random
import time
import requests


urls = ['https://miro.medium.com/max/1200/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg'] * 30

# def sleeper(t, idx):
#     time.sleep(t)
#     print(f'{idx} sleeper woken up sleep for {t}')
#     return idx


def download_file(url: str, file_name: str):
    result = requests.get(url)
    ext = url.split('.')[-1]
    with open(f'{file_name}.{ext}', 'wb') as file:
        file.write(result.content)
    return file_name


executor = ThreadPoolExecutor(max_workers=30)


futures = [executor.submit(download_file, url, idx) for idx, url in enumerate(urls)]


for future in as_completed(futures):
    print(future.result())