import websockets
import asyncio
clients = []

data = {}

with open("D:\maps\mapsImages - Copy\geoToImg.txt","r") as f:
    for _ in range(0, 200000):
        x, y, v, w = f.readline().split(" ")
        data[x + " " + y] = v + " " + w.replace("\n", "")


autoIdSocket = {}
async def handle_websocket(websocket, path):
    try:
        clients.append(websocket)
        print(websocket)
        while True:
            msg: str = await websocket.recv()

            if msg.isdigit():
                autoIdSocket[websocket] = msg
                continue

            for a in clients:
                await a.send(str(autoIdSocket.get(websocket)) + ":" + str(data.get(msg)))

    except websockets.ConnectionClosed:
        clients.remove(websocket)
        print("error occurred")

async def main():
    async with websockets.serve(handle_websocket, "localhost", 8765):
        print("reached here")
        await asyncio.Future()


asyncio.run(main())
