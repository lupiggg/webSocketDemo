import asyncio
import websockets

# Set of connected clients
connected = set()

async def handler(websocket, path):
    # Register client
    connected.add(websocket)
    try:
        async for message in websocket:
            # Broadcast incoming message to all connected clients
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
    finally:
        # Unregister client
        connected.remove(websocket)

# Start server
start_server = websockets.serve(handler, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
