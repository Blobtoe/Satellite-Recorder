from bottle import post, run, request, response
from datetime import datetime
import os
import asyncio
import websockets

def log(msg):
    print(datetime.now().strftime("%Y %b. %m %H:%M:%S"), ":", str(msg))

'''
@post("/record")
def record():
    if "center_frequency" or "samplerate" or "format" or "duration" not in request.keys():
        log("Not all neccessary parameters given.")
        response.status = 400
        return "Not all neccessary parameters given."
    
    os.system
    return

run(host="localhost", port=8000, debug=True)
'''

def record(center_frequency, samplerate, format, duration, gain):
    os.system(f"timeout {duration} rtl_fm -M {format} -s {samplerate} -f {center_frequency} -g {gain} recording")

async def echo(websocket, path):
    async for message in websocket:
        record(107.1, 100000, "wav", 200, 49.6)

async def main():
    async with websockets.serve(echo, "localhost", 8000):
        await asyncio.Future()

asyncio.run(main())