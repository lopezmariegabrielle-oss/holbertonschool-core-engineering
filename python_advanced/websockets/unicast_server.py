"""Module for a WebSocket unicast server."""

import asyncio
import websockets


connected_clients = set()


async def unicast_handler(websocket):
    """Handle a single client connection and manage its messages."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")

    finally:
        connected_clients.remove(websocket)


async def main():
    """Start the WebSocket unicast server on localhost at port 8765."""
    async with websockets.serve(unicast_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
