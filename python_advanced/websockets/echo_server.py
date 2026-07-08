"""Module pour un serveur WebSocket Echo de base."""
import asyncio
import websockets


async def echo_handler(websocket):
    """Gère la connexion d'un client et renvoie ses messages en écho."""
    while True:
        message = await websocket.recv()
        await websocket.send(message)


async def main():
    """Démarre le serveur WebSocket sur localhost au port 8765."""
    async with websockets.serve(echo_handler, "localhost", 8765):
        print("Serveur Echo démarré sur ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
