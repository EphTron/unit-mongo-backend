import asyncio
import websockets
from requests import get

ip = get('https://api.ipify.org').text

async def hello():
    # uri = "ws://warden.cygnus.uberspace.de:9000"
    uri = "ws://warden.uber.space:9000/test"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

async def haggle():
    # uri = "ws://warden.cygnus.uberspace.de:9000"
    uri = "wss://ephtron.uber.space/unit-backend"
    async with websockets.connect(uri) as websocket:
        #json_command = '{"command":"add","username":"ephra","ip":"'+str(ip)+'","key":"test"}'

        #await websocket.send(json_command)
        #answer = await websocket.recv()

        #print(answer)
        json_command2 = '{"command":"echo", "username":"ephra", "message":"test"}'
        await websocket.send(json_command2)

        greeting = await websocket.recv()
        print(f"< {greeting}")


asyncio.get_event_loop().run_until_complete(haggle())
asyncio.get_event_loop().run_forever()