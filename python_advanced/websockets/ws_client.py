#!/usr/bin/env python3
"""Module for a basic WebSocket client."""

import asyncio
import os
import sys
import websockets


async def connect_and_send(uri, message):
    """Connect to the server, send a message, and print the response."""
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        réponse = await websocket.recv()
        return réponse


if __name__ == "__main__":
    uri = os.environ.get("WS_URI", "ws://localhost:8765")

    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = os.environ.get("WS_MESSAGE", "demo")

    res = asyncio.run(connect_and_send(uri, message))
    sys.stdout.write(res)
