import asyncio
import os


class Sleek:
    """
    A simple asyncio server that listens on a Unix socket
    """

    def __init__(self, socket_name="/tmp/sleek.sock"):
        """Initialize the server with a socket name"""
        self.socket_name = socket_name

    async def handle_client(self, reader, writer):
        """Handle a client connection"""
        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break  # Client closed the connection
                response = "Hello from Python"
                writer.write(response.encode())
                await writer.drain()

        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            print("Closing the connection")
            writer.close()
            await writer.wait_closed()

    async def run(self):
        """Start the server and listen for incoming connections"""
        if os.path.exists(self.socket_name):
            os.remove(self.socket_name)

        server = await asyncio.start_unix_server(
            self.handle_client, path=self.socket_name
        )

        print(f"[sleek] Serving on {self.socket_name}")
        async with server:
            await server.serve_forever()
