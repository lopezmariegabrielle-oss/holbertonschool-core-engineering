#!/usr/bin/env python3
"""Module for a WebSocket broadcast server."""

import asyncio
import websockets


connected_clients = set()


async def broadcast_handler(websocket):
    """Handle a single client connection and broadcast its messages."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients:
                await client.send(f"B:{message}")
    finally:
        connected_clients.remove(websocket)


async def main():
    """Start the WebSocket broadcast server on localhost at port 8765."""
    async with websockets.serve(broadcast_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
