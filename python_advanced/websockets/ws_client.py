"""Module for a basic WebSocket client."""

import asyncio
import websockets


async def hello():
    """Connect to the server, send a message, and print the response."""
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(response)


if __name__ == "__main__":
    asyncio.run(hello())
