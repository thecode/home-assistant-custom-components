"""Script to test connection."""
import asyncio
import logging
import ssl

from websockets.client import connect as ws_connect  # pip install websockets==10.4

HOST = "192.168.1.39"
NON_SSL_PORT = 3000
SSL_PORT = 3001


async def main():
    """Test connection using non SSL & SSL."""
    fmt = (
        "%(asctime)s.%(msecs)03d %(levelname)s (%(threadName)s) [%(name)s] %(message)s"
    )
    logging.basicConfig(level=logging.DEBUG, format=fmt)
    logger = logging.getLogger(__name__)

    ssl_context = ssl.SSLContext()

    logger.info("Connect without SSL start")

    try:
        ws = await ws_connect(
            f"ws://{HOST}:{NON_SSL_PORT}",
            ping_interval=5,
            ping_timeout=20,
            open_timeout=2,
            close_timeout=2,
            max_size=None,
        )
    except Exception as err:
        logger.error("Connect without SSL error: %r", err)

    try:
        ws.close()
    except Exception:
        pass

    logger.info("Connect without SSL end")
    logger.info("Connect using SSL start")

    try:
        ws1 = await ws_connect(
            f"wss://{HOST}:{SSL_PORT}",
            ping_interval=5,
            ping_timeout=20,
            open_timeout=2,
            close_timeout=2,
            max_size=None,
            ssl=ssl_context,
        )
    except Exception as err:
        logger.error("Connect using SSL error: %r", err)

    logger.info("Connect using SSL end")

    try:
        ws1.close()
    except Exception:
        pass


if __name__ == "__main__":
    asyncio.run(main())
