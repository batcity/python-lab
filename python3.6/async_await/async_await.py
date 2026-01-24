import time
import requests
import asyncio

start = time.time()
requests.get("http://google.com")
requests.get("http://google.com")
requests.get("http://google.com")
end = time.time()
print("time taken to hit google three times: ", end - start)


# Now do the same thing as before but asynchronously so that it's quicker