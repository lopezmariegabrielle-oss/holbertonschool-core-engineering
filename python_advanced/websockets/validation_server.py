#!/usr/bin/env python3
"""Module for a WebSocket server with message validation."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Receive messages, validate them, and echo back the result."""
    try:
        async for message in websocket:
            cleaned_message = message.strip()

            if not cleaned_message:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


async def main():
    """Start the WebSocket validation server on localhost at port 8765."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
