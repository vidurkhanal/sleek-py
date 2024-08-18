import asyncio
import os
import signal
import gc


class Sleek:
    """
    A simple asyncio server that listens on a Unix socket
    """

    def __init__(self, socket_name="/tmp/sleek.sock", max_connections=100):
        """Initialize the server with a socket name and maximum connections"""
        self.socket_name = socket_name
        self.max_connections = max_connections
        self.connection_count = 0

    async def handle_client(self, reader, writer):
        """Handle a client connection"""
        self.connection_count += 1
        try:
            while True:
                data = await reader.read(4 * 1024)
                if not data:
                    break

                writer.write(data)
                await writer.drain()
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            print("Closing the connection")
            writer.close()
            await writer.wait_closed()
            self.connection_count -= 1

    async def run(self):
        """Start the server and listen for incoming connections"""
        if os.path.exists(self.socket_name):
            os.remove(self.socket_name)

        server = await asyncio.start_unix_server(
            self.handle_client, path=self.socket_name
        )

        print(f"[sleek] Serving on {self.socket_name}")
        async with server:
            asyncio.create_task(self._periodic_gc())
            try:
                await server.serve_forever()
            except asyncio.CancelledError:
                print("[sleek] Server shutting down")
                server.close()
                await server.wait_closed()
                raise

    async def _periodic_gc(self):
        """Run garbage collection periodically"""
        while True:
            await asyncio.sleep(120)
            gc.collect()
            print("[sleek] Garbage collection completed.")
