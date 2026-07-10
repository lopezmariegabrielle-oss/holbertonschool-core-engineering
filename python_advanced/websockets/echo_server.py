#!/usr/bin/env python3
"""Module for a basic WebSocket Echo server."""

import asyncio
import websockets


async def connection_handler(websocket):
    """Receive a connection and echo back any message it receives."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the WebSocket server on localhost at port 8765."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
