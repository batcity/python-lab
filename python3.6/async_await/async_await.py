import time
import requests
import asyncio
import httpx

start = time.time()
requests.get("http://google.com")
requests.get("http://google.com")
requests.get("http://google.com")
end = time.time()
print("time taken to hit google three times: ", end - start)

# Now do the same thing as before but asynchronously so that it's quicker

# TODO: modify this method to actually print the responses so we know it's working
async def fetch_web_page_asynchronously():
    async with httpx.AsyncClient() as client:
        # create a list of coroutines/tasks
        # there's three tasks that fetch google.com
        tasks = [client.get("http://google.com") for _ in range(3)]
        
        # TODO: figure out what await actually means
        responses = await asyncio.gather(*tasks)
    
start = time.time()
asyncio.run(fetch_web_page_asynchronously())
end = time.time()
print("time taken to hit google three times: ", end - start)