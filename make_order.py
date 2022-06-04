import random
import requests
import time


banana = '🍌'
apple = '🍎'
pear = '🍐'

items = [banana, apple, pear, 'foo', 'bar']

for _ in range(1000):
    # Make a random order
    order = items[random.randrange(len(items))]


    url = "http://127.0.0.1:8000"

    response = requests.post(
        url=f'{url}/order',
        params={
            'order': order
        }
    )

    print(f'Status code: {response.status_code}, order: {order}')
    time.sleep(1)
