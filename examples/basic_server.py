import asyncio
from sleek_py import Sleek

if __name__ == "__main__":
    server = Sleek()
    asyncio.run(server.run())
