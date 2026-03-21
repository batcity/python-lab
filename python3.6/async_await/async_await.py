import time
import requests
import asyncio
import httpx

start = time.time()
requests.get("https://www.google.com")
requests.get("https://www.google.com")
requests.get("https://www.google.com")
end = time.time()
print("time taken to hit google three times consecutively: ", end - start)

# Now this method does the same thing as before but asynchronously so that it's quicker
async def fetch_web_page_asynchronously():
    async with httpx.AsyncClient() as client:
        # create a list of coroutines/tasks
        # there's three tasks that fetch google.com
        tasks = [client.get("https://www.google.com") for _ in range(3)]
        
        responses = await asyncio.gather(*tasks)
        
        for i, response in enumerate(responses):
            print(f"Response status code {i}:")
            print(response.status_code)
    
start = time.time()
asyncio.run(fetch_web_page_asynchronously())
end = time.time()
print("time taken to hit google three times concurrently: ", end - start)