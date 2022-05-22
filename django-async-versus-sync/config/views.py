import asyncio
import aiohttp
from django.shortcuts import render

import requests
import time


async def fetch(session, url):
    async with session.get(url) as response:
        assert response.status == 200
        return await response.json()


async def async_home_view(request):
    start_time = time.time()

    url_list = [
        ('people', 'https://swapi.dev/api/people/'),
        ('starships', 'https://swapi.dev/api/starships/'),
    ]

    async with aiohttp.ClientSession() as client:
        tasks = []

        for key, url in url_list:
            task = asyncio.ensure_future(fetch(client, url))
            tasks.append(task)

        results = await asyncio.gather(*tasks)


    total_time = time.time() - start_time

    context = {
        'people': results[0],
        'starships': results[1],
        'total_time': total_time,
    }

    return render(request, 'home.html', context)




def home_view(request):
    start_time = time.time()

    data = []

    url_list = [
        'https://swapi.dev/api/people/',
        'https://swapi.dev/api/starships/',
    ]

    for url in url_list:
        response = requests.get(url)
        results = response.json()
        data.append(results)

    total_time = time.time() - start_time

    context = {
        'people': data[0],
        'starships': data[1],
        'total_time': total_time,
    }

    return render(request, 'home.html', context)