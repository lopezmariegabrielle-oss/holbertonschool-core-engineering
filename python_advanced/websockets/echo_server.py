import asyncio
import websockets


async def echo_handler(websocket):
    while True:
        message = await websocket.recv()
        await websocket.send(message)


async def main():
    async with websockets.serve(echo_handler, "localhost", 8765):
        print("Serveur Echo démarré sur ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
